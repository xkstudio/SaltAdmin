#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio

from BaseHandler import BaseHandler

# 404页面
class Page404Handler(BaseHandler):
    def get(self):
        self.render('page/404.html', title="404")

# 空白页
class BlankHandler(BaseHandler):
    def get(self):
        self.render('page/blank.html', title="Blank")