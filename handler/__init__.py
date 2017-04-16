#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KK Studio

import index
import host
import user
import page
import salt_handler
import test

route = [
    (r'/',index.IndexHandler),
    (r'/host',host.IndexHandler),
    (r'/host/detail',host.HostDetailHandler),
    (r'/host/group',host.GroupHandler),
    (r'/host/create',host.CreateHostHandler),
    (r'/user/login',user.LoginHandler),
    (r'/user/logout',user.LogoutHandler),
    (r'/user/profile',user.ProfileHandler),
    (r'/user/passwd',user.PasswdHandler),
    (r'/user',user.UserHandler),
    (r'/salt/master',salt_handler.MasterHandler),
    (r'/salt/key',salt_handler.KeyHandler),
    (r'/page/404.html',page.Page404Handler),
    (r'/page/blank.html',page.BlankHandler),
    (r'/test',test.TestHandler),
    #(r'.*',page.Page404Handler), # 默认路由定位到404
]