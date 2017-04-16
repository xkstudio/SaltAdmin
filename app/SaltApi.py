#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KK Studio

import tornado.httpclient
import urllib
import json

class Api:

    def __init__(self,url='',username='salt',password='123456',eauth='pam'):
        self.url = url
        self.username = username
        self.password = password
        self.eauth = eauth

    def http(self,url,method='GET',data=None,headers=None):
        tornado.httpclient.AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient") # pycurl
        http_client = tornado.httpclient.HTTPClient()
        options = {
            'method': method.upper(),
            'validate_cert': False,
            'allow_ipv6': False,
            'connect_timeout': 10,
            'request_timeout': 300
        }
        # Set UA: user_agent='' or headers={'User-Agent':'MyUA'}
        if headers:
            options['headers'] = headers
        if options['method'] == 'GET' and data:
            url += '?' + urllib.urlencode(data)
        elif options['method'] == 'POST' and data:
            options['body'] = urllib.urlencode(data)
        response = http_client.fetch(url,**options)
        content_type = response.headers.get('Content-Type')
        if 'json' in content_type:
            resp_data = json.loads(response.body)
        else:
            resp_data = response.body
        return {'code':response.code,'body':resp_data}


if __name__ == '__main__':
    api = Api()
    print api.http('http://admin1.congxue.com/api/test/hello','POST',{'foo':'234'})
