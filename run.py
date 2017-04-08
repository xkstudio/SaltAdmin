#!/usr/bin/python
# -*- coding:utf8 -*-
# Powered By KStudio

from app.SaltAdmin import SaltAdmin

if __name__ == "__main__":
    host = '0.0.0.0'
    port = 8888
    app = SaltAdmin(host,port)
    app.run()