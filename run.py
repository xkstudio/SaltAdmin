#!/usr/bin/python
# -*- coding:utf8 -*-
# Powered By XK-Studio

from app import SaltAdmin
from config.settings import settings
from config.settings import db as db_conf
from handler.route import urls

if __name__ == "__main__":
    host = '0.0.0.0'
    port = 8888
    app = SaltAdmin.App(host,port,urls,settings,db_conf)
    app.run()
