#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KK Studio

from BaseHandler import BaseHandler
from app.SaltApi import Api

from tornado.httpclient import AsyncHTTPClient
import tornado

# Test Page
class TestHandler(BaseHandler):

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        url = 'http://admin1.test.com/api/test/hello?foo=2'

        client = AsyncHTTPClient()
        resp = yield client.fetch(url)
        self.write(resp.body)

        #resp = Api().http(url)
        #self.write(resp)

        self.finish()
