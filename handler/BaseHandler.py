#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio

import tornado

class BaseHandler(tornado.web.RequestHandler):

    # 数据库
    @property
    def db(self):
        return self.application.db

    def hello(self):
        pass