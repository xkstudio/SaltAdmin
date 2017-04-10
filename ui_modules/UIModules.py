#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KK Studio

from tornado.web import UIModule


# Test
class Test(UIModule):

    def render(self,foo):
        return foo


# 导航Nav
class Nav(UIModule):

    def render(self,url):
        return self.render_string("ui_modules/nav.html",url=url)
