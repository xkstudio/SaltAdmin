#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KK Studio

from BaseHandler import BaseHandler
from app.SaltApi import Api

# Test Page
class TestHandler(BaseHandler):
    def get(self):
        url = 'https://api.github.com'
        data = Api().http(url)
        return self.jsonReturn(data)
        #self.write('Test')
