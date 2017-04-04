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
        uid = user.id
        if password != user.password:
            return self.jsonReturn({'code': -3, 'msg': '密码错误'})
        return self.jsonReturn({'code': 0, 'msg': 'Success'})