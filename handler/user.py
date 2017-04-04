#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio
# 用户管理

from BaseHandler import BaseHandler
from model.models import User

class UserHandler(BaseHandler):
    def get(self):
        data = self.db.query(User).all()
        gender = {1:'男', 2:'女'}
        self.render('user/index.html', title="用户管理",data=data,gender=gender)

# 用户登录
class LoginHandler(BaseHandler):
    def get(self):
        #self.write("This is SlatAdmin Login Page.")
        self.render('user/login.html', title="Login")

    def post(self):
        username = self.get_argument("username",None)
        password = self.get_argument("password",None)
        remember = self.get_argument("remember","no")
        if not username or not password:
            return self.jsonReturn({'code':-1,'msg':'参数错误'})
        user = self.db.query(User).filter_by(username=username).first()
        if not user:
            return self.jsonReturn({'code': -2, 'msg': '用户名错误'})
        if password != user.password:
            return self.jsonReturn({'code': -3, 'msg': '密码错误'})
        # 验证通过，创建会话
        self.create_session(user,remember)
        url = self.get_argument("next","/")
        return self.jsonReturn({'code': 0, 'msg': 'Success', 'url': url})

    def create_session(self,user,remember):
        #记录登录信息
        headers = self.request.headers
        login_ip = self.request.remote_ip
        login_ua = headers.get('User-Agent')
        login_data = {
            "login_time": self.time,
            "login_ua": login_ua,
            "login_ip": login_ip
            #"login_location": user.login_location
        }
        self.db.query(User).filter_by(id=user.id).update(login_data)
        self.db.commit()
        #写Session
        session = {
            "uid": user.id,
            "username": user.username,
            "nickname": user.nickname,
            "login_time": user.login_time,
            "login_ua": user.login_ua,
            "login_ip": user.login_ip,
            "login_location": user.login_location
        }
        self.set_session(session)