#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio
# 主机管理

from BaseHandler import BaseHandler
from tornado.web import authenticated as Auth
from model.models import Host
from model.models import HostGroup
from model.models import or_


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
        # 检测重复
        chk = self.db.query(Host).filter(or_(Host.hostname==data['hostname'],Host.ip==data['ip'],Host.minion_id==data['minion_id'])).first()
        if chk:
            if chk.hostname == data['hostname']:
                msg = u'主机名重复'
            elif chk.minion_id == data['minion_id']:
                msg = u'Salt ID 重复'
            elif chk.ip == data['ip']:
                msg = u'IP地址重复'
            else:
                msg = u'主机重复'
            return self.jsonReturn({'code': -2, 'msg': msg, 'hid': chk.id})
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

    @Auth
    def post(self):
        hid = self.get_argument('hid', None)
        data = {
            'hostname': self.get_argument('hostname',None),
            'minion_id': self.get_argument('smid',None),
            'ip': self.get_argument('ip',None),
            'host_group': self.get_argument('group',None),
            'host_desc': self.get_argument('desc',None),
            'os': self.get_argument('os',None),
            'cpu': self.get_argument('cpu',None),
            'hdd': self.get_argument('hdd',None),
            'mem': self.get_argument('mem',None),
            'vendor': self.get_argument('vendor',None),
            'model': self.get_argument('model',None),
            'snum': self.get_argument('snum',None),
            'tag': self.get_argument('tag',None)
        }
        # 检测重复
        chk = self.db.query(Host).filter(or_(Host.hostname==data['hostname'],Host.ip==data['ip'],Host.minion_id==data['minion_id'])).first()
        if chk and int(chk.id) != int(hid):
            if chk.hostname == data['hostname']:
                msg = u'主机名重复'
            elif chk.minion_id == data['minion_id']:
                msg = u'Salt ID 重复'
            elif chk.ip == data['ip']:
                msg = u'IP地址重复'
            else:
                msg = u'主机重复'
            return self.jsonReturn({'code': -2, 'msg': msg, 'hid': chk.id})
        ret = self.db.query(Host).filter_by(id=hid).update(data)  # <type 'long'> - 1
        self.db.commit()
        if ret:
            code = 0
            msg = 'Success'
        else:
            self.db.rollback()
            code = -1
            msg = u'保存失败'
        return self.jsonReturn({'code': code, 'msg': msg})

