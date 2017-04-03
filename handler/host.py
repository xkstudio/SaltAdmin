#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio
# 主机管理

from BaseHandler import BaseHandler

class HostHandler(BaseHandler):
    def get(self):
        self.write("This is SlatAdmin Host Page.")