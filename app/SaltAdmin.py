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

class App():

    def __init__(self,host,port,urls,settings,processes=4):
        self.__version__ = '2.0.0'
        self.host = host
        self.port = port
        self.urls = urls
        self.settings = settings
        if platform.system() == "Linux":  #根据操作系统类型来确定是否启用多线程
            self.processes = processes # 当processes>1时，PeriodicCallback定时任务会响相应的执行多次
        else:
            self.processes = 1

    #打印版本号到控制台
    def print_version(self):
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print '[%s] SaltAdmin %s' % (now,self.__version__)

    #多线程模式
    def run(self):
        self.print_version() # 启动时打印版本号
        http_sockets = tornado.netutil.bind_sockets(self.port, self.host)
        tornado.process.fork_processes(num_processes=self.processes)
        http_server = tornado.httpserver.HTTPServer(request_callback=SaltAdmin(self.urls,self.settings), xheaders=True)
        http_server.add_sockets(http_sockets)
        tornado.ioloop.IOLoop.instance().start()