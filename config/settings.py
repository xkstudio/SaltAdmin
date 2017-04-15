#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KK Studio

from tornado.options import define, options
import tornado.options

define("host", default='0.0.0.0', help="Listen on the given IP", type=str)
define("port", default=8888, help="Run on the given port", type=int)

tornado.options.parse_command_line()

# Call options.*** should be after the parse_command_line()

config = {
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'db': 'saltadmin2',
        'user': 'test',
        'passwd': 'test',
        'charset': 'utf8'
    },
    'redis': {
        'host': '127.0.0.1',
        'port': 6503,
        'password': '',
        'db': '0'
    },
    'host': options.host,
    'port': options.port,
    'app_settings': dict(
        template_path = 'view',
        static_path = 'static',
        static_url_prefix = '/static/',
        xsrf_cookies = False,
        cookie_secret = "db884468559f4c432bf1c1775f3dc9da",
        cookie_name = '_ksid',
        session_prefix = "_k_session_",
        session_expires = 7200,
        login_url = "/user/login",
        default_lang = "en_US",
        debug = True,
        autoreload = True
    )
}