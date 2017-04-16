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

        # Test Command: ab -n 1000 -c 100 http://127.0.0.1:8888/test

        url = 'http://admin1.test.com/api/test/hello?foo=2'

        client = AsyncHTTPClient()
        resp = yield client.fetch(url)
        self.write(resp.body)

        #resp = Api().http(url)
        #self.write(resp)

        self.finish()
