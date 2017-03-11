#!/usr/bin/python
# -*- coding:utf8 -*-
# Powered By XK-Studio

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("This is SlatAdmin")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

def run(port=8888):
    app = make_app()
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    run()
