#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KK Studio

from BaseHandler import BaseHandler

# Test Page
class TestHandler(BaseHandler):
    def get(self):
        self.write('Test')
