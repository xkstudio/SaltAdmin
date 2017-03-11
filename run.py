#!/usr/bin/python
# -*- coding:utf8 -*-
# Powered By XK-Studio

from app import SaltAdmin
from config import settings
from handler import route

if __name__ == "__main__":
    host = '0.0.0.0'
    port = 8888
    app = SaltAdmin.App(host,port,route.urls,settings.settings)
    app.run()
