#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio
# 主机管理

from BaseHandler import BaseHandler
from model.models import Host
from model.models import HostGroup


class IndexHandler(BaseHandler):
    def get(self):
        data = self.db.query(Host).all()
        grps = self.db.query(HostGroup).all()
        groups = {}
        for i in grps:
            groups[i.id] = i.group_name
        status = {1:"正常",2:"未知"}
        self.render('host/index.html',data=data,groups=groups,status=status)


class GroupHandler(BaseHandler):
    def get(self):
        data = self.db.query(HostGroup).all()
        self.render('host/group.html',data=data)

class CreateHostHandler(BaseHandler):
    def get(self):
        groups = self.db.query(HostGroup).all()
        self.render('host/create_host.html',groups=groups)