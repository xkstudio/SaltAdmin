#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio
# 控制中心

import tornado

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("This is SlatAdmin Index Page.")


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("This is SlatAdmin Login Page.")