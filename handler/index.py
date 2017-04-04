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
            'tornado': tornado_verion,
            'saltadmin': '2.0.0'
        }
        return data

    @Auth
    def get(self):
        data = self.get_system_info()
        self.render('index/index.html',title="Hello",data=data)
