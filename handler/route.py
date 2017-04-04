#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio
import index
import host
import user
import page

urls = [
    (r'/',index.IndexHandler),
    (r'/host',host.IndexHandler),
    (r'/host/group',host.GroupHandler),
    (r'/host/create',host.CreateHostHandler),
    (r'/user/login',user.LoginHandler),
    (r'/user/logout',user.LogoutHandler),
    (r'/user/profile',user.ProfileHandler),
    (r'/user/passwd',user.PasswdHandler),
    (r'/user',user.UserHandler),
    (r'/page/404.html',page.Page404Handler),
    (r'/page/blank.html',page.BlankHandler),
    (r'.*',page.Page404Handler), # 默认路由定位到404
]