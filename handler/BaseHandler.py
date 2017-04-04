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
        title = "%s - %s" % (status_code, self._reason)
        if status_code == 404: # 捕获404
            self.render('page/error.html',title=title)
        elif status_code == 500: # 500可以正常捕获，404好像不行
            #print self.settings.get("serve_traceback")
            msg = ''
            if 'exc_info' in kwargs:
                for i in kwargs['exc_info']:
                    #print type(i)
                    msg += "<p>%s</p>" % str(i)
            self.render('page/error.html', title=title, code=status_code, msg=msg)
        else:
            self.render('page/error.html', title=title, code=status_code, msg=status_code)


    # 数据库
    @property
    def db(self):
        return self.application.db

    def hello(self):
        pass