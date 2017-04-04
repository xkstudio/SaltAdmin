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
        # 请求逻辑处理结束时关闭数据库连接，如果不关闭可能会造成MySQL Server has gone away 2006错误
        self.db.close()

    # 数据库
    @property
    def db(self):
        return self.application.db

    def hello(self):
        pass