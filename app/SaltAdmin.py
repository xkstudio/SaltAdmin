#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio

import tornado
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.netutil
import tornado.process
import tornado.options
import time

class SaltAdmin(tornado.web.Application):

    def __init__(self,handlers,settings):
        tornado.web.Application.__init__(self, handlers, **settings)
        tornado.options.parse_command_line()
        #每分钟执行一次
        tornado.ioloop.PeriodicCallback(self.test, 1 * 60 * 1000).start()

    def test(self):
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print '[%s] Test' % now



class App():

    def __init__(self,host,port,urls,settings,processes=2):
        self.host = host
        self.port = port
        self.urls = urls
        self.settings = settings
        self.processes = processes

    def run(self):
        http_sockets = tornado.netutil.bind_sockets(self.port, self.host)
        tornado.process.fork_processes(num_processes=self.processes)
        http_server = tornado.httpserver.HTTPServer(request_callback=SaltAdmin(self.urls,self.settings), xheaders=True)
        http_server.add_sockets(http_sockets)
        tornado.ioloop.IOLoop.instance().start()