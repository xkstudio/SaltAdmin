#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio
# 用户管理

from BaseHandler import BaseHandler
from tornado.web import authenticated as Auth
from model.models import User

class UserHandler(BaseHandler):
    @Auth
    def get(self):
        page = int(self.get_argument('page', 1))
        line = int(self.get_argument('line', 50))
        offset = (page - 1) * line
        data = self.db.query(User).offset(offset).limit(line).all()
        gender = {1:u'男', 2:u'女'}
        self.render('user/index.html', title=u"用户管理",data=data,gender=gender)

# 用户登录
class LoginHandler(BaseHandler):
    def get(self):
        if not self.session.isGuest:
            return self.redirect('/') # 已登录则跳转到首页
        next = self.get_argument("next", "/")
        self.render('user/login.html', next=next)

    def post(self):
        username = self.get_argument("username",None)
        password = self.get_argument("password",None)
        remember = self.get_argument("remember","no")
        if not username or not password:
            return self.jsonReturn({'code':-1,'msg':u'参数错误'})
        profile = self.db.query(User).filter_by(username=username).first()
        if not profile:
            return self.jsonReturn({'code': -2, 'msg': u'用户名或密码错误'})
        if self.md5(password) != profile.password:
            return self.jsonReturn({'code': -2, 'msg': u'用户名或密码错误'})
        ##### 验证通过逻辑 #####
        self.create_session(profile,remember) # Create Session
        # 记录登录信息
        headers = self.request.headers
        login_ua = headers.get('User-Agent')
        login_ip = self.request.remote_ip
        login_data = {
            "login_time": self.time,
            "login_ua": login_ua,
            "login_ip": login_ip
            # "login_location": login_location
        }
        self.db.query(User).filter_by(id=profile.id).update(login_data)
        self.db.commit()
        # 跳转登录前的URL
        url = self.get_argument("next","/")
        return self.jsonReturn({'code': 0, 'msg': 'Success', 'url': url})


    def create_session(self,data,remember):
        sid = self.session.gen_session_id()
        self.session.data = {
            "uid": data.id,
            "username": data.username,
            "nickname": data.nickname,
            "lang": data.lang,
            "login_time": data.login_time,
            "login_ua": data.login_ua,
            "login_ip": data.login_ip,
            "login_location": data.login_location
        }
        self.session.isGuest = False
        #self.session.save() # Why don't save? See self._on_finish !!
        if remember == "yes":
            expires_days = 15  # Remember Session 15 days
        else:
            expires_days = None
        self.set_secure_cookie(self.cookie_name, sid, expires_days)


# 注销登录
class LogoutHandler(BaseHandler):
    def get(self):
        self.session.remove()
        self.clear_cookie(self.cookie_name)
        self.redirect(self.get_login_url())


# 我的资料
class ProfileHandler(BaseHandler):
    @Auth
    def get(self):
        profile = self.db.query(User).filter_by(id=self.uid).first()
        self.render('user/profile.html',profile=profile)

    @Auth
    def post(self):
        data = {
            "nickname": self.get_argument("nickname", None),
            "gender": self.get_argument("gender", None),
            "email": self.get_argument("email", None),
            "phone": self.get_argument("phone", None),
            "dept": self.get_argument("dept", None),
            "lang": self.get_argument("lang", 'zh_CN'),
            "update_time": self.time
        }
        # 数据校验
        if not data['nickname']:
            return self.jsonReturn({'code': -1, 'msg': u'姓名不能空'})
        if data['gender'] not in ['1','2']:
            return self.jsonReturn({'code': -1, 'msg': u'参数错误'})
        self.db.query(User).filter_by(id=self.uid).update(data) # <type 'long'> - 1
        self.db.commit() # <type 'NoneType'> - None
        return self.jsonReturn({'code': 0, 'msg': 'Success'})


# 修改密码
class PasswdHandler(BaseHandler):
    @Auth
    def get(self):
        self.render('user/passwd.html')