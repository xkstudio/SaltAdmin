#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio
# 控制中心

from BaseHandler import BaseHandler

class IndexHandler(BaseHandler):
    def get(self):
        foo = self.redis.get('test')
        #self.write("This is SlatAdmin Index Page.")
        self.render('index/index.html',title="Hello",foo=foo)


class LoginHandler(BaseHandler):
    def get(self):
        #self.write("This is SlatAdmin Login Page.")
        self.render('index/login.html', title="Login")