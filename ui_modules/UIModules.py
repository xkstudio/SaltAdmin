#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KK Studio

from tornado.web import UIModule


# Test
class Test(UIModule):

    def render(self,foo):
        return foo


# 导航Nav
class Nav(UIModule):

    url_none = 'javascript:void(0);'

    nav = [
        {
            'url': '/',
            'name': '控制中心',
            'icon': 'icon-wrench',
            'sub': []
        },
        {
            'url': '',
            'name': '主机管理',
            'icon': 'icon-layers',
            'sub': [
                {
                    'url': '/host',
                    'name': '主机清单',
                    'icon': ''
                },
                {
                    'url': '/host/group',
                    'name': '主机分组',
                    'icon': ''
                },
                {
                    'url': '/host/create',
                    'name': '创建主机',
                    'icon': ''
                }
            ]
        },
        {
            'url': '',
            'name': '任务管理',
            'icon': 'icon-bar-chart',
            'sub': [
                {
                    'url': '#',
                    'name': '命令下发',
                    'icon': ''
                },
                {
                    'url': '#',
                    'name': '文件分发',
                    'icon': ''
                }
            ]
        },
        {
            'url': '',
            'name': '系统管理',
            'icon': 'icon-wrench',
            'sub': [
                {
                    'url': '#',
                    'name': '系统设置',
                    'icon': ''
                },
                {
                    'url': '#',
                    'name': '用户管理',
                    'icon': ''
                }
                ,
                {
                    'url': '#',
                    'name': '版本升级',
                    'icon': ''
                }
            ]
        },
        {
            'url': '',
            'name': '页面管理',
            'icon': 'icon-grid',
            'sub': [
                {
                    'url': '/page/404.html',
                    'name': '404页面',
                    'icon': 'icon-bulb'
                },
                {
                    'url': '/page/blank.html',
                    'name': '空白页面',
                    'icon': 'icon-bar-chart'
                }
                ,
                {
                    'url': '/user/login',
                    'name': '登录页面',
                    'icon': 'icon-bulb'
                }
            ]
        },
        {
            'url': '',
            'name': '关于',
            'icon': 'icon-info',
            'sub': [
                {
                    'url': '#',
                    'name': '系统信息',
                    'icon': ''
                },{
                    'url': '#',
                    'name': '技术交流',
                    'icon': ''
                },{
                    'url': '#',
                    'name': 'Bug提交',
                    'icon': ''
                }
            ]
        }
    ]


    def gen_sub_nav(self,data,url=''):
        HL = False
        html = '<ul class="sub-menu">'
        for i in data:
            if url == i['url']:
                css_class = 'nav-item active open' # High Light Style
                HL = True
            else:
                css_class = 'nav-item'
            html += '<li class="%s"><a href="%s" class="nav-link">' % (css_class,i['url'])
            if i['icon']:
                html += '<i class="%s"></i>' % i['icon']
            html += '<span class="title">%s</span></a></li>' % i['name']
        html += '</ul>'
        return {'HL': HL, 'html': html}


    def render(self,url):
        for i in self.nav:
            hl = False # High Light
            data = self.gen_sub_nav(i['sub'])
        return self.render_string("ui_modules/nav.html",url=url)
