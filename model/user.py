#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio

from sqlalchemy import Column, String, INTEGER, VARCHAR, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(INTEGER,primary_key=True)
    username = Column(VARCHAR(32))
    password = Column(VARCHAR(64))
    email = Column(VARCHAR(32))
    phone = Column(VARCHAR(32))
    nickname = Column(VARCHAR(32))
    role = Column(VARCHAR(32))
    create_time = Column(INTEGER)
    update_time = Column(INTEGER)
    status = Column(INTEGER)