#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KK Studio

import tornado
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.netutil
import tornado.process
import tornado.options
import tornado.locale
import platform
import redis
from tornado.log import gen_log
from DB import Database
from handler.page import Page404Handler
from config.settings import config
from handler import route
from Template import TemplateLoader


class App(tornado.web.Application):

    def __init__(self,handlers,settings,conf,log):
        self.log = log
        settings['default_handler_class'] = Page404Handler # 404
        # 每10秒执行一次
        #tornado.ioloop.PeriodicCallback(self.test, 1 * 10 * 1000).start()
        # App Version
        self.__version__ = conf['version']
        # Template
        tpl_loader = TemplateLoader(settings['template_path'],False)
        # Init Tornado App
        tornado.web.Application.__init__(self, handlers, template_loader=tpl_loader.Loader(), **settings)
        # 数据库
        self.db = self.get_db(conf['db'])
        # Redis
        self.redis = self.get_redis(conf['redis'])
        # Load Locale
        self.__load_locale(settings['default_lang'])

    def get_redis(self,conf):
        return redis.Redis(**conf)

    def get_db(self,conf):
        db = Database(**conf)
        return db.db_session()

    #def test(self):
    #    print "Test"

    # Load Locale
    def __load_locale(self,default_lang):
        tornado.locale.load_translations('locales')
        tornado.locale.set_default_locale(default_lang)

class SaltAdmin():

    def __init__(self,processes=4):
        self.__version__ = '2.0.0'
        self.config = config
        self.config['version'] = self.__version__
        self.host = config['host']
        self.port = config['port']
        self.urls = route
        self.log = gen_log
        if platform.system() == "Linux":  #根据操作系统类型来确定是否启用多线程
            self.processes = processes # 当processes>1时，PeriodicCallback定时任务会响相应的执行多次
        else:
            self.processes = 1

    # 多线程模式
    def run(self):
        self.log.info('SaltAdmin %s' % self.__version__) # 启动时打印版本号
        self.log.info('Listen Port: %s' % self.port)
        http_sockets = tornado.netutil.bind_sockets(self.port, self.host)
        tornado.process.fork_processes(num_processes=self.processes)
        http_server = tornado.httpserver.HTTPServer(request_callback=App(self.urls,self.config['app_settings'],self.config,self.log), xheaders=True)
        http_server.add_sockets(http_sockets)
        tornado.ioloop.IOLoop.instance().start()