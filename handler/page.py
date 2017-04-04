#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio

from BaseHandler import BaseHandler

class Page404Handler(BaseHandler):
    def get(self):
        self.render('page/404.html', title="404")