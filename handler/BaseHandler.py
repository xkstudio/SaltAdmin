#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio

import tornado
import os
import time
import json
import hashlib

class BaseHandler(tornado.web.RequestHandler):

    # 初始化函数
    def initialize(self):
        # 当前请求时间
        self.time = int(time.time())
        self.time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.time))
        # Current URL
        self.url = self.get_route()
        # Session
        self.session = None # 用户未登录标识
        self.init_session()
        # Version
        self.app_version = self.application.__version__

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

    # Log Instance
    @property
    def log(self):
        return self.application.log

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

    # 格式化时间戳
    def format_time(self,timstamp=None):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timstamp))


    # 获取当前登录用户
    def get_current_user(self):
        return self.session


    # Session初始化
    def init_session(self):
        self.session_key  = self.settings.get('session_key')
        self.session_expires  = self.settings.get('session_expires')
        self.cookie_name = self.settings.get('cookie_name')
        self.cookie_value = self.get_secure_cookie(self.cookie_name)
        if self.cookie_value:
            self.session_id = self.session_key + self.cookie_value
            self.session = self.get_session()
            if self.session:
                # 刷新Seesion过期时间
                self.redis.expire(self.session_id, self.session_expires)
        else:
            #self.cookie_value = self.gen_session_id()
            #self.set_secure_cookie(self.cookie_name,self.cookie_value)
            #self.session_id = self.session_key + self.cookie_value
            self.session_id = None


    def get_session(self):
        session = self.redis.get(self.session_id)
        if not session:
            return None
        session = json.loads(session) # 字符串转字典
        return session


    def set_session(self):
        self.redis.set(self.session_id,json.dumps(self.session),self.session_expires) # 后端Session


    def create_session(self,session,expires_days=None):
        self.cookie_value = self.gen_session_id()
        self.session_id = self.session_key + self.cookie_value
        self.session = session
        self.set_session()
        self.set_secure_cookie(self.cookie_name, self.cookie_value, expires_days)  # 前端Cookie


    # 销毁Session
    def remove_session(self):
        if self.session: # Session存在
            self.redis.delete(self.session_id)
            self.clear_cookie(self.cookie_name)


    # 生成SessionID
    def gen_session_id(self):
        return hashlib.sha1('%s%s' % (os.urandom(16), time.time())).hexdigest()


    # MD5计算
    def md5(self,text):
        s = hashlib.md5()
        s.update(text)
        return s.hexdigest()


    # 获取当前路由
    def get_route(self):
        uri = self.request.uri.split('?')
        return uri[0]

    # 重写获取用户语言的方法
    def get_user_locale(self):
        #user_lang = self.get_argument('lang', 'zh')
        default_lang = self.settings.get('default_lang')
        if self.session:
            user_lang = self.session.get('lang')
        else:
            user_lang = default_lang # Default Language
        if user_lang in ['en_US','zh_CN']:
            return tornado.locale.get(user_lang)
        else:
            return tornado.locale.get(default_lang) # Default Language
