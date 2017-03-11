#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio
import index
import host

urls = [
    (r'/(|index)/?',index.IndexHandler),
    (r'/login',index.LoginHandler),
    (r'/host',host.HostHandler)
]