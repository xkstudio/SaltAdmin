#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio

import tornado
import time
import hashlib
from app.Session import Session
from ui_modules.Nav import Nav

class BaseHandler(tornado.web.RequestHandler):

    # 初始化函数
    def initialize(self):
        # 当前请求时间
        self.time = int(time.time())
        self.time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.time))
        # Current URL
        self.url = self.get_route()
        # Session
        self.init_session()
        # Version
        self.app_version = self.application.__version__

    # 后面的方法如果重写on_finish方法，需要调用_on_finish
    def _on_finish(self):
        # 更新Session
        self.session.save()
        # 请求逻辑处理结束时关闭数据库连接，如果不关闭可能会造成MySQL Server has gone away 2006错误
        self.db.close()

    # 重载on_finish
    def on_finish(self):
        self._on_finish()

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
    def format_time(self,timestamp=None):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))


    # Session初始化
    def init_session(self):
        prefix = self.settings.get('session_prefix')
        expires = self.settings.get('session_expires')
        self.cookie_name = self.settings.get('cookie_name')
        self.sid = self.get_secure_cookie(self.cookie_name)
        self.session = Session(prefix,self.sid,expires,self.redis)


    # 重写get_current_user
    def get_current_user(self):
        if not self.session.isGuest and self.session.data:
            return self.session.data
        else:
            return None


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
        if not self.session.isGuest: # Login
            user_lang = self.session.get('lang')
        else:
            user_lang = default_lang # Default Language
        if user_lang in ['en_US','zh_CN']:
            return tornado.locale.get(user_lang)
        else:
            return tornado.locale.get(default_lang) # Default Language


    # Nav UI
    def get_nav(self):
        return Nav().gen_nav(self.url)
