#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio
# 主机管理

from BaseHandler import BaseHandler
from tornado.web import authenticated as Auth
from model.models import Host
from model.models import HostGroup
from model.models import SaltMaster
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
        page = int(self.get_argument('page',1))
        line = int(self.get_argument('line',100))
        offset = (page-1)*line
        data = self.db.query(Host).offset(offset).limit(line).all()
        groups = get_groups(self.db)
        status = {
            0: u'<span class="label label-default"> 未知 </span>',
            1: u'<span class="label label-success"> 在线 </span>',
            2 :u'<span class="label label-danger"> 离线 </span>'}
        self.render('host/index.html',data=data,groups=groups,status=status)


class GroupHandler(BaseHandler):
    @Auth
    def get(self):
        data = get_groups(self.db)
        self.render('host/group.html',data=data)

    @Auth
    def post(self):
        gid = self.get_argument('gid',None)
        name = self.get_argument('name',None)
        f = self.get_argument('f',None) # c = create, u = update, d = delete
        if not gid and not name and not f:
            return self.jsonReturn({'code': -1, 'msg': u'参数错误'})
        if f == 'c': # Create a New Group
            chk = self.db.query(HostGroup).filter_by(group_name=name).first()
            if chk:
                return self.jsonReturn({'code': -2, 'msg': u'分组重复'})
            hg = HostGroup(group_name=name,create_time=self.time,update_time=self.time)
            self.db.add(hg)
            self.db.commit()
            gid = hg.id
            if gid:
                code = 0
                msg = '成功新增分组'
            else:
                self.db.rollback()
                gid = 0
                code = -3
                msg = u'保存失败'
            return self.jsonReturn({'code': code, 'msg': msg, 'gid': gid})
        elif f == 'u': # Update Group Info
            chk = self.db.query(HostGroup).filter_by(group_name=name).all()
            if chk:
                for i in chk:
                    if i.id != int(gid) and i.group_name == name:
                        return self.jsonReturn({'code': -2, 'msg': u'分组重复', 'gid': i.id})
            ret = self.db.query(HostGroup).filter_by(id=gid).update({'group_name':name,'update_time':self.time})  # <type 'long'> - 1
            self.db.commit()
            if ret:
                code = 0
                msg = '保存成功'
            else:
                self.db.rollback()
                code = -3
                msg = u'保存失败'
            return self.jsonReturn({'code': code, 'msg': msg})
        elif f == 'd': # Delete a Group
            chk = self.db.query(HostGroup).filter_by(id=gid).first()
            if not chk:
                return self.jsonReturn({'code': -4, 'msg': u'分组不存在'})
            # Check Host
            chk = self.db.query(Host).filter_by(host_group=gid).first()
            if chk:
                return self.jsonReturn({'code': -5, 'msg': u'请先清空该分组的主机'})
            # Delete Group
            self.db.query(HostGroup).filter_by(id=gid).delete()
            self.db.commit()
            return self.jsonReturn({'code': 0, 'msg': u'删除成功'})
        else:
            return self.jsonReturn({'code': -1, 'msg': u'参数错误'})


class CreateHostHandler(BaseHandler):
    @Auth
    def get(self):
        groups = get_groups(self.db)
        saltmaster = self.db.query(SaltMaster).all()
        if not saltmaster:
            saltmaster = [{'id':0,'hostname':u'请先添加SaltMaster'}]
        self.render('host/create_host.html',groups=groups,saltmaster=saltmaster)

    @Auth
    def post(self):
        data = {
            'hostname': self.get_argument('hostname',None),
            'minion_id': self.get_argument('minion_id',None),
            'master_id': self.get_argument('master_id',None),
            'ip': self.get_argument('ip',None),
            'host_group': self.get_argument('group',None),
            'host_desc': self.get_argument('desc',None),
            'create_time': self.time,
            'status': 0 # Default status is 0
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
        saltmaster = self.db.query(SaltMaster).all()
        if not saltmaster:
            saltmaster = [{'id':0,'hostname':u'请先添加SaltMaster'}]
        self.render('host/host_detail.html',data=data,groups=groups,saltmaster=saltmaster)

    @Auth
    def post(self):
        hid = self.get_argument('hid', None)
        data = {
            'hostname': self.get_argument('hostname',None),
            'minion_id': self.get_argument('minion_id',None),
            'master_id': self.get_argument('master_id',None),
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
            'tag': self.get_argument('tag',None),
            'update_time': self.time
        }
        # 检测重复
        chk = self.db.query(Host.id,Host.hostname,Host.minion_id,Host.ip).filter(or_(Host.hostname==data['hostname'],Host.ip==data['ip'],Host.minion_id==data['minion_id'])).all()
        if chk:
            for row in chk:
                if int(row.id) != int(hid):
                    if row.hostname == data['hostname']:
                        msg = u'主机名重复'
                    elif row.minion_id == data['minion_id']:
                        msg = u'Salt ID 重复'
                    elif row.ip == data['ip']:
                        msg = u'IP地址重复'
                    else:
                        msg = u'主机重复'
                    return self.jsonReturn({'code': -2, 'msg': msg, 'hid': row.id})
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

