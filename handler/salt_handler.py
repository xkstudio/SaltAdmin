#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KK Studio

from BaseHandler import BaseHandler
from model.models import SaltMaster


# Salt-Master管理
class MasterHandler(BaseHandler):
    def get(self):
        data = self.db.query(SaltMaster).all()
        self.render('salt/master.html',data=data)


# Salt-Key管理
class KeyHandler(BaseHandler):
    def get(self):
        self.render('salt/key.html')
