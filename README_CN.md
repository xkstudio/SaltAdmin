SaltAdmin
=========

![SaltAdmin](https://github.com/luxiaok/SaltAdmin/raw/master/static/images/SaltAdminLogo.jpg)

基于[SaltStack](https://github.com/saltstack/salt)的自动化运维平台

Powered By [KK Studio](http://github.com/kkstu)

版本: **2.0-Alpha**

旧版 (v1.0) https://github.com/luxiaok/SaltAdmin


## 概览

![SaltAdmin](http://git.luxiaok.com:82/xiaok/SaltAdmin/raw/bdcb7db9ce31438300a5ae78be9f0624fb0fe9f4/static/img/screenshot/login.jpg)


## 依赖组件

- [Torweb](https://github.com/kkstu/Torweb)：1.0+

- [Tornado](http://www.tornadoweb.org/)：4.0+

- [SaltStack](https://github.com/saltstack/salt)：>= 2015.1.0

- [SQLAlchemy](http://www.sqlalchemy.org/)：1.1.8

- [Jinja2](http://jinja.pocoo.org/)：2.9+

- [MySQL](http://www.percona.com/)：Percona-Server 5.5/5.6

- [MySQL-python](http://pypi.python.org/pypi/MySQL-python)：1.2.5+

- [Redis-Py](https://github.com/andymccurdy/redis-py)：2.10+

- [Python](http://www.python.org)：2.6.x/2.7.x


## 安装部署

#### 获取SaltAdmin源码

> git clone https://github.com/kkstu/SaltAdmin.git

#### 安装依赖组件

- yum install MySQL-python

- pip install tornado

- pip install redis

- pip install jinja2

- pip install SQLAlchemy

#### 部署Saltstack

##### RedHat/CentOS系列

-  yum install salt-master

-  yum install salt-minion

##### Ubuntu系列

- apt-get install salt-master

- apt-get install salt-minion

> 更多Saltstack部署信息请参考官网 https://repo.saltstack.com/


## 贡献代码

正式版2.0发布之后才接受代码贡献


## 支持和帮助

请通过工单(Issues)提交您遇到的问题或需要反馈的建议或Bug。

https://github.com/kkstu/SaltAdmin/issues


## 技术交流

#### 微信

![Python运维圈](https://github.com/luxiaok/SaltAdmin/raw/master/static/images/ops_circle_qrcode.jpg)

#### QQ群

459457262


#### 开发团队官网

http://studio.luxiaok.com


## 开源协议

MIT

协议详情：[LICENSE](http://git.luxiaok.com:82/xiaok/SaltAdmin/src/master/LICENSE)
