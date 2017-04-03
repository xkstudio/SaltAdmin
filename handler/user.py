#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio
# 用户管理

from BaseHandler import BaseHandler

class UserHandler(BaseHandler):
    def get(self):
        #self.write("This is SlatAdmin Host Page.")
        self.render('user/index.html', title="用户管理")