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
import platform
import time

class SaltAdmin(tornado.web.Application):

    def __init__(self,handlers,settings):
        tornado.web.Application.__init__(self, handlers, **settings)
        #后台日志高亮输出
        tornado.options.parse_command_line()
        #每10秒执行一次
        tornado.ioloop.PeriodicCallback(self.test, 1 * 10 * 1000).start()

    def test(self):
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print '[%s] Test' % now


def test():
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print '[%s] Test' % now

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class App():

    def __init__(self,host,port,urls,settings,processes=1):
        self.host = host
        self.port = port
        self.urls = urls
        self.settings = settings
        self.processes = processes # 当processes>1时，PeriodicCallback定时任务会响相应的执行多次

    # 多线程模式1
    def run(self):
        http_sockets = tornado.netutil.bind_sockets(self.port, self.host)
        tornado.process.fork_processes(num_processes=self.processes)
        http_server = tornado.httpserver.HTTPServer(request_callback=SaltAdmin(self.urls,self.settings), xheaders=True)
        http_server.add_sockets(http_sockets)
        tornado.ioloop.IOLoop.instance().start()

    #多线程模式2
    def run2(self):
        app = tornado.web.Application([(r"/", MainHandler),])
        http_server = tornado.httpserver.HTTPServer(app)
        http_server.bind(8888)
        if (platform.system() == "Linux"):  # 判断操作系统类型
            http_server.start(4)  # linux 系统开启多进程
        else:
            http_server.start()  # windows 系统只启动单进程
        tornado.ioloop.PeriodicCallback(test, 1 * 10 * 1000).start()
        tornado.ioloop.IOLoop.instance().start()