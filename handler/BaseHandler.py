#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio

import tornado

class BaseHandler(tornado.web.RequestHandler):

    # 初始化函数
    def initialize(self):
        pass

    # 重载on_finish
    def on_finish(self):
        pass

    # 数据库
    @property
    def db(self):
        return self.application.db

    def hello(self):
        pass