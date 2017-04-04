#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio
# 控制中心

from BaseHandler import BaseHandler
from tornado.web import authenticated as Auth

class IndexHandler(BaseHandler):
    @Auth
    def get(self):
        self.render('index/index.html',title="Hello",foo='bar')
