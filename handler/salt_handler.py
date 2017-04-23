#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KK Studio

from BaseHandler import BaseHandler
from model.models import SaltMaster
from tornado.web import authenticated as Auth
from model.models import or_


# Salt-Master管理
class MasterHandler(BaseHandler):

    @Auth
    def get(self):
        data = self.db.query(SaltMaster).all()
        self.render('salt/master.html',data=data)

    @Auth
    def post(self):
        f = self.get_argument('f', None)
        _id = self.get_argument('id', None)
        data = {
            'hostname': self.get_argument('hostname', None),
            'api': self.get_argument('api_url', None),
            'username': self.get_argument('api_username', None),
            'password': self.get_argument('api_password', None)
        }
        if not data['hostname'] or f not in ['c','u'] or not data['username']:
            return self.jsonReturn({'code': -1, 'msg': u'参数错误'})
        if f == 'c':
            if not data['password']:
                return self.jsonReturn({'code': -2, 'msg': u'SaltAPI密码不能为空'})
            chk = self.db.query(SaltMaster).filter(or_(SaltMaster.hostname == data['hostname'], SaltMaster.api == data['api'])).first()
            if chk:
                return self.jsonReturn({'code': -3, 'msg': u'SaltMaster重复'})
            data['create_time'] = self.time
            s = SaltMaster(**data)
            self.db.add(s)
            self.db.commit()
            if s.id:
                code = 0
                msg = 'Success'
            else:
                self.db.rollback()
                code = -1
                msg = u'保存失败'
            return self.jsonReturn({'code': code, 'msg': msg})
        else: # Update
            if not _id:
                return self.jsonReturn({'code': -1, 'msg': u'参数错误'})
            chk = self.db.query(SaltMaster).filter(or_(SaltMaster.hostname == data['hostname'], SaltMaster.api == data['api'])).all()
            if chk:
                for i in chk:
                    if i.id != int(_id):
                        if i.hostname == data['hostname'] or data['api']:
                            return self.jsonReturn({'code': -3, 'msg': u'SaltMaster重复'})
            if not data['password']:
                del(data['password']) # 密码为空时不修改密码
            ret = self.db.query(SaltMaster).filter_by(id=_id).update(data)  # <type 'long'> - 1
            self.db.commit()
            if ret:
                code = 0
                msg = u'保存成功'
            else:
                self.db.rollback()
                code = -3
                msg = u'保存失败'
            return self.jsonReturn({'code': code, 'msg': msg})



# Salt-Key管理
class KeyHandler(BaseHandler):

    @Auth
    def get(self):
        data = self.db.query(SaltMaster).all()
        self.render('salt/key.html',data=data)
