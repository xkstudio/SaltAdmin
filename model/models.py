#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio

from sqlalchemy import Column, Integer, SmallInteger, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

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