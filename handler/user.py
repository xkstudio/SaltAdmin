#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio
# 用户管理

from BaseHandler import BaseHandler
from model.user import User

class UserHandler(BaseHandler):
    def get(self):
        data = self.db.query(User).all()
        for i in data:
            print "*"*10
            print "UID: %s" % i.id
            print "Username: %s" % i.username
            print "Password: %s" % i.password
            print "E-mail: %s" % i.email
        #self.write("This is SlatAdmin Host Page.")
        self.render('user/index.html', title="用户管理")