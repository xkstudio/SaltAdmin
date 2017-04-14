#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio
# 主机管理

from BaseHandler import BaseHandler
from tornado.web import authenticated as Auth
from model.models import Host
from model.models import HostGroup


# 获取主机分组
def get_groups(db):
    all = db.query(HostGroup).all()
    groups = {}
    for i in all:
        groups[i.id] = {'group_name':i.group_name,'hosts_count':i.hosts_count,'gid':i.id}
    return groups


class IndexHandler(BaseHandler):
    @Auth
    def get(self):
        data = self.db.query(Host).all()
        groups = get_groups(self.db)
        status = {1:u"正常",2:u"未知"}
        self.render('host/index.html',data=data,groups=groups,status=status)


class GroupHandler(BaseHandler):
    @Auth
    def get(self):
        data = get_groups(self.db)
        self.render('host/group.html',data=data)


class CreateHostHandler(BaseHandler):
    @Auth
    def get(self):
        groups = get_groups(self.db)
        self.render('host/create_host.html',groups=groups)

    @Auth
    def post(self):
        data = {
            'hostname': self.get_argument('hostname',None),
            'minion_id': self.get_argument('smid',None),
            'ip': self.get_argument('ip',None),
            'host_group': self.get_argument('group',None),
            'host_desc': self.get_argument('desc',None),
            'create_time': self.time
        }
        h = Host(**data)
        self.db.add(h)
        self.db.commit()
        hid = h.id
        if hid:
            code = 0
            msg = 'Success'
        else:
            self.db.rollback()
            hid = 0
            code = -1
            msg = 'Error'
        return self.jsonReturn({'code': code, 'msg': msg, 'hid': hid})


# 主机详情
class HostDetailHandler(BaseHandler):
    @Auth
    def get(self):
        hid = self.get_argument("hid",None)
        groups = get_groups(self.db)
        data = self.db.query(Host).filter_by(id=hid).first()
        self.render('host/host_detail.html',data=data,groups=groups)