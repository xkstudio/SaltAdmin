#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio

from sqlalchemy import Column, Integer, SmallInteger, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(VARCHAR(32),nullable=False)
    password = Column(VARCHAR(64),nullable=False)
    email = Column(VARCHAR(32),nullable=True)
    phone = Column(VARCHAR(32),nullable=True)
    nickname = Column(VARCHAR(32),nullable=True)
    gender = Column(SmallInteger,nullable=True) # 性别
    dept = Column(VARCHAR(32),nullable=True) # 部门
    role = Column(VARCHAR(32),nullable=True)
    create_time = Column(Integer,nullable=True)
    update_time = Column(Integer,nullable=True)
    status = Column(SmallInteger,nullable=True)