#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio

import tornado
import os
import time
from hashlib import sha1

class BaseHandler(tornado.web.RequestHandler):

    # 初始化函数
    def initialize(self):
        # 当前请求时间
        self.time = int(time.time())
        self.time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.time))

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

    # Redis
    @property
    def redis(self):
        return self.application.redis

    # 返回Json
    def jsonReturn(self,data):
        self.set_header('Content-Type', 'application/json')
        self.write(data)

    def get_current_user(self):
        uid = self.get_secure_cookie("k_auth_token")
        if not uid: return None
        return uid

    # 生成SessionID
    def gen_ksid(self):
        return lambda: sha1('%s%s' % (os.urandom(16), time.time())).hexdigest()