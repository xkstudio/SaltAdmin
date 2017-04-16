#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KK Studio

import tornado.httpclient
import urllib
import json

class Api:

    def __init__(self,url='',username='salt',password='123456',eauth='pam'):
        self._url = url
        self._username = username
        self._password = password
        self._eauth = eauth

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
            options['body'] = json.dumps(data)
        try:
            response = http_client.fetch(url,**options)
            content_type = response.headers.get('Content-Type')
        except tornado.httpclient.HTTPError as e:
            #print dir(e)
            return {'code':e.code,'msg':e.message}
        except Exception, e:
            #print e
            return {'code': -2}
        if 'json' in content_type:
            resp_data = json.loads(response.body)
        else:
            resp_data = response.body
        return {'code':response.code,'body':resp_data}


    def get_token(self):
        body = {'username':self._username,'password':self._password,'eauth':self._eauth}
        headers = {'Accept':'application/json','Content-Type':'application/json'}
        data = self.http(self._url+'/login','POST',body,headers)
        token_data = {}
        if data.get('code',None) == 200:
            body = data['body']
            if body.get('return',None):
                token_data = body['return'][0]
        return token_data


if __name__ == '__main__':
    api = Api('http://192.168.1.69:8081')
    print api.get_token()
