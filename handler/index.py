#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio
# 控制中心

from BaseHandler import BaseHandler
from tornado.web import authenticated as Auth
from model.models import User

class IndexHandler(BaseHandler):
    @Auth
    def get(self):
        foo = self.redis.get('test')
        #self.write("This is SlatAdmin Index Page.")
        print self.request.headers
        print self.time
        print self.time_str
        self.render('index/index.html',title="Hello",foo=foo)


class LoginHandler(BaseHandler):
    def get(self):
        #self.write("This is SlatAdmin Login Page.")
        self.render('index/login.html', title="Login")

    def post(self):
        username = self.get_argument("username",None)
        password = self.get_argument("password",None)
        if not username or not password:
            return self.jsonReturn({'code':-1,'msg':'参数错误'})
        user = self.db.query(User).filter_by(username=username).first()
        if not user:
            return self.jsonReturn({'code': -2, 'msg': '用户名错误'})
        if password != user.password:
            return self.jsonReturn({'code': -3, 'msg': '密码错误'})
        self.jsonReturn({'code': 0, 'msg': 'Success'})