#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio

import tornado
import os
import time
import json
from hashlib import sha1

class BaseHandler(tornado.web.RequestHandler):

    # 初始化函数
    def initialize(self):
        # 当前请求时间
        self.time = int(time.time())
        self.time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.time))
        # Session
        self.gen_session()

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
        ksid_name = self.settings.get('ksid_name')
        ksid = self.get_secure_cookie(ksid_name)
        user = self.get_session(ksid)
        if not user and 'uid' not in user:
            return None
        return user['username']

    def get_session(self,ksid):
        session_key = self.settings.get('session_key')
        user = self.redis.get(session_key + ksid)
        if not user:
            return None
        user = json.loads(user) # 字符串转字典
        return user


    # 生成SessionID
    def gen_ksid(self):
        return sha1('%s%s' % (os.urandom(16), time.time())).hexdigest()


    # Session控制
    def gen_session(self):
        ksid_name = self.settings.get('ksid_name')
        expires = self.settings.get('session_expires')
        ksid = self.get_secure_cookie(ksid_name)
        if not ksid:
            ksid = self.gen_ksid()
            self.set_secure_cookie(ksid_name, ksid, expires=None)
        self.ksid = ksid