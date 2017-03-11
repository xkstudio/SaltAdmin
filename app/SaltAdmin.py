#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio

import tornado
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.netutil
import tornado.process

class SaltAdmin(tornado.web.Application):

    def __init__(self,handlers,settings):
        tornado.web.Application.__init__(self, handlers, **settings)



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