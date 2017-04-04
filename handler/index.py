#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio
# 控制中心

import tornado
from BaseHandler import BaseHandler
from tornado.web import authenticated as Auth

class IndexHandler(BaseHandler):

    # 获取系统信息
    def get_system_info(self):
        tornado_verion = tornado.version
        data = {
            'tornaod': tornado_verion
        }
        return data

    @Auth
    def get(self):
        info = self.get_system_info()
        self.render('index/index.html',title="Hello",info=info)
