#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KK Studio

from sqlalchemy import Column, Integer, SmallInteger, VARCHAR, or_
from sqlalchemy.ext.declarative import declarative_base

or_ = or_

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(VARCHAR(32),nullable=False,unique=True)
    password = Column(VARCHAR(64),nullable=False)
    email = Column(VARCHAR(32),nullable=True)
    phone = Column(VARCHAR(32),nullable=True)
    nickname = Column(VARCHAR(32),nullable=True)
    gender = Column(SmallInteger,nullable=True) # 性别
    dept = Column(VARCHAR(32),nullable=True) # 部门
    role = Column(VARCHAR(32),nullable=True)
    lang = Column(VARCHAR(32),nullable=True) # Language
    login_time = Column(Integer,nullable=True)
    login_ua = Column(VARCHAR(600),nullable=True)
    login_ip = Column(VARCHAR(64),nullable=True)
    login_location = Column(VARCHAR(32),nullable=True)
    create_time = Column(Integer,nullable=True)
    update_time = Column(Integer,nullable=True)
    status = Column(SmallInteger,nullable=True)


class Host(Base):
    __tablename__ = 'hosts'

    id = Column(Integer,primary_key=True,autoincrement=True)
    hostname = Column(VARCHAR(64), nullable=False, unique=True)
    master_id = Column(Integer, nullable=True)
    minion_id = Column(VARCHAR(64), nullable=True, unique=True)
    ip = Column(VARCHAR(64), nullable=False)
    os = Column(VARCHAR(64), nullable=True)
    vendor = Column(VARCHAR(64), nullable=True)
    model = Column(VARCHAR(64), nullable=True)
    cpu = Column(VARCHAR(64), nullable=True)
    hdd = Column(VARCHAR(64), nullable=True)
    mem = Column(VARCHAR(64), nullable=True)
    snum = Column(VARCHAR(64), nullable=True)
    tag = Column(VARCHAR(64), nullable=True)
    host_desc = Column(VARCHAR(64), nullable=True)
    host_group = Column(Integer, nullable=True)
    create_time = Column(Integer, nullable=True)
    update_time = Column(Integer, nullable=True)
    status = Column(SmallInteger, nullable=True)


class HostGroup(Base):
    __tablename__ = 'hosts_groups'

    id = Column(Integer,primary_key=True,autoincrement=True)
    group_name = Column(VARCHAR(64), nullable=False,unique=True)
    hosts_count = Column(Integer,nullable=False,default=0)
    create_time = Column(Integer,nullable=True)
    update_time = Column(Integer,nullable=True)