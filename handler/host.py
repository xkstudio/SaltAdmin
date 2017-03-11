#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio
# 主机管理

import tornado

class HostHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("This is SlatAdmin Host Page.")