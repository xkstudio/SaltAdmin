#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio
# 主机管理

from BaseHandler import BaseHandler

class IndexHandler(BaseHandler):
    def get(self):
        self.render('host/index.html')


class GroupHandler(BaseHandler):
    def get(self):
        self.render('host/group.html')