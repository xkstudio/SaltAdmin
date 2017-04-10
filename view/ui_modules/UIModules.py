#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KK Studio

from tornado.web import UIModule

# 导航Nav
class Nav(UIModule):

    def render(self,foo):
        msg = "%s,Nav!" % foo
        return msg