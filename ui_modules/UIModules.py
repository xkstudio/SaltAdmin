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
            'url': url_none,
            'name': '主机管理',
            'icon': 'icon-screen-desktop',
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
            'url': url_none,
            'name': 'SaltStack',
            'icon': 'icon-layers',
            'sub': [
                {
                    'url': '/salt/key',
                    'name': 'SaltKey',
                    'icon': ''
                },
                {
                    'url': '/salt/service',
                    'name': 'Salt服务管理',
                    'icon': ''
                }
            ]
        },
        {
            'url': url_none,
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
            'url': url_none,
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
            'url': url_none,
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
            'url': url_none,
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


    # 生成二级菜单
    def gen_sub_nav(self,data,url=''):
        HL = False
        if not data: # 二级菜单为空
            return {'HL': HL, 'html': ''}
        html = '<ul class="sub-menu">'
        for i in data:
            if url == i['url']:
                css_class = 'nav-item active open' # High Light Style
                HL = True
            else:
                css_class = 'nav-item'
            html += '<li class="%s"><a href="%s" class="nav-link">' % (css_class,i['url'])
            if i['icon']:
                html += '<i class="%s"></i> ' % i['icon']
            html += '<span class="title">%s</span></a></li>' % i['name']
        html += '</ul>'
        return {'HL': HL, 'html': html}

    # 生成菜单
    def gen_nav(self,url):
        html = ''
        for i in self.nav:
            sub = self.gen_sub_nav(i['sub'],url)
            if i['url'] == url or sub['HL']:
                html += '<li class="%s">' % 'nav-item active open'
                html += '<a href="%s" class="nav-link nav-toggle">' % i['url']
                html += '<i class="%s"></i><span class="title">%s</span>' % (i['icon'],i['name'])
                if sub['html']:
                    html += '<span class="arrow open"></span><span class="selected"></span></a>'
                else:
                    html += '<span class="arrow"></span><span class="selected"></span></a>'
            else:
                html += '<li class="%s">' % 'nav-item'
                html += '<a href="%s" class="nav-link nav-toggle">' % i['url']
                html += '<i class="%s"></i><span class="title">%s</span>' % (i['icon'], i['name'])
                html += '<span class="arrow"></span></a>'
            html += sub['html'] # Sub Menu Html
            html += '</li>'
        return html


    def render(self,url):
        data = self.gen_nav(url)
        return self.render_string("ui_modules/nav.html",data=data)
