#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio
# 用户管理

from BaseHandler import BaseHandler
from model.models import User

class UserHandler(BaseHandler):
    def get(self):
        data = self.db.query(User).all()
        gender = {1:'男', 2:'女'}
        self.render('user/index.html', title="用户管理",data=data,gender=gender)