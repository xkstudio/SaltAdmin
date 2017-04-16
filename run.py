#!/usr/bin/python
# -*- coding:utf8 -*-
# Powered By KK Studio

from app.SaltAdmin import SaltAdmin

if __name__ == "__main__":
    app = SaltAdmin()
    #app.run() # Multi Processes Model
    app.run_single()