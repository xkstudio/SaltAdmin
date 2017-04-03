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
from Log import Log
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class App(tornado.web.Application):

    def __init__(self,handlers,settings,db_conf):
        tornado.web.Application.__init__(self, handlers, **settings)
        #后台日志高亮输出
        tornado.options.parse_command_line()
        #每10秒执行一次
        #tornado.ioloop.PeriodicCallback(self.test, 1 * 10 * 1000).start()
        #封装数据库
        engine = create_engine('mysql+mysqldb://%s:%s@%s:%s/%s?charset=%s' %
            (db_conf['user'], db_conf['pass'], db_conf['host'], db_conf['port'], db_conf['db'], db_conf['charset']),
            encoding='utf-8', echo=False,
            pool_size=100, pool_recycle=10)
        self.db = scoped_session(sessionmaker(bind=engine))

    def test(self):
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print '[%s] Test' % now

class SaltAdmin():

    def __init__(self,host,port,urls,settings,db_conf,processes=4):
        _log = Log()
        self.log = _log.info
        self.__version__ = '2.0.0'
        self.host = host
        self.port = port
        self.urls = urls
        self.settings = settings
        self.db_conf = db_conf
        if platform.system() == "Linux":  #根据操作系统类型来确定是否启用多线程
            self.processes = processes # 当processes>1时，PeriodicCallback定时任务会响相应的执行多次
        else:
            self.processes = 1

    #多线程模式
    def run(self):
        self.log('SaltAdmin %s' % self.__version__) # 启动时打印版本号
        self.log('Listen Port: %s' % self.port)
        http_sockets = tornado.netutil.bind_sockets(self.port, self.host)
        tornado.process.fork_processes(num_processes=self.processes)
        http_server = tornado.httpserver.HTTPServer(request_callback=App(self.urls,self.settings,self.db_conf), xheaders=True)
        http_server.add_sockets(http_sockets)
        tornado.ioloop.IOLoop.instance().start()