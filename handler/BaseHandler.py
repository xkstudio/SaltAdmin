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

    # 重载write_error方法
    def write_error(self, status_code, **kwargs):
        if status_code == 404: # 捕获404
            self.render('page/404.html')
        elif status_code == 500: # 500可以正常捕获，404好像不行
            self.render('page/500.html')
        else:
            self.render('page/error.html',code=status_code,msg=self._re_reason)

    # 数据库
    @property
    def db(self):
        return self.application.db

    def hello(self):
        pass