#!/usr/bin/python
# -*- coding:utf8 -*-
# Powered By XK-Studio

from app.SaltAdmin import SaltAdmin
from config.settings import settings
from config.settings import config
from handler.route import urls

if __name__ == "__main__":
    host = '0.0.0.0'
    port = 8888
    app = SaltAdmin(host,port,urls,settings,config)
    app.run()
