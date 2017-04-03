#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio

import time

class Log:

    def log_time(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S] ', time.localtime())

    def echo(self,msg):
        print "%s%s" % (self.log_time(),msg)

    def info(self,msg):
        self.echo(msg)