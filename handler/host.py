#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio
# 主机管理

from BaseHandler import BaseHandler
from model.models import Host


class IndexHandler(BaseHandler):
    def get(self):
        data = self.db.query(Host).all()
        self.render('host/index.html',data=data)


class GroupHandler(BaseHandler):
    def get(self):
        self.render('host/group.html')