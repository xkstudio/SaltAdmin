#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KK Studio

from BaseHandler import BaseHandler


# Salt-Master管理
class MasterHandler(BaseHandler):
    def get(self):
        self.render('salt/master.html')


# Salt-Key管理
class KeyHandler(BaseHandler):
    def get(self):
        self.render('salt/key.html')
