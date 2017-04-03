#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio
# 用户管理

from BaseHandler import BaseHandler
from model.user import User

class UserHandler(BaseHandler):
    def get(self):
        data = self.db.query(User).all()
        self.render('user/index.html', title="用户管理",data=data)