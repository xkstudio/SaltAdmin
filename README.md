SaltAdmin2
=========

![SaltAdmin](https://github.com/luxiaok/SaltAdmin/raw/master/static/images/SaltAdminLogo.jpg)

Automated operation and maintenance platform based on [SaltStack](https://github.com/saltstack/salt).

Powered By [KK Studio](http://github.com/kkstu)

Version: **2.0-Alpha**


## Overview

![SaltAdmin](http://git.luxiaok.com:82/xiaok/SaltAdmin/src/master/static/img/screenshot/login.jpg)


## Features

- Host assets management automation

- Host monitoring (Batch)

- Host service management

- Soft Package management

- Execute remote commands in batches

- Transport files in batches

- Custom jobs management


## Dependency Component

- [Torweb](https://github.com/kkstu/Torweb)：1.0+

- [Tornado](http://www.tornadoweb.org/)：4.0+

- [SaltStack](https://github.com/saltstack/salt)：>= 2015.1.0

- [SQLAlchemy](http://www.sqlalchemy.org/)：1.1.8

- [Jinja2](http://jinja.pocoo.org/)：2.9+

- [MySQL](http://www.percona.com/)：Percona-Server 5.5/5.6

- [MySQL-python](http://pypi.python.org/pypi/MySQL-python)：1.2.5+

- [Redis-Py](https://github.com/andymccurdy/redis-py)：2.10+

- [Python](http://www.python.org)：2.6.x/2.7.x


## Deployment

#### Get started

> git clone https://github.com/kkstu/SaltAdmin.git

#### Install Component

- yum install MySQL-python

- pip install tornado

- pip install redis

- pip install jinja2

- pip install SQLAlchemy

#### Deploying Saltstack

##### RedHat/CentOS

-  yum install salt-master

-  yum install salt-minion

##### Ubuntu

- apt-get install salt-master

- apt-get install salt-minion

> More about Saltstack deployment documents see the https://repo.saltstack.com/.


## Documents

- See the [docs](docs).

- [简体中文](README.md)


## Contributors

After the version 2.0-Stable release.


## Technology Communications

#### Wechat

![Python运维圈](https://github.com/luxiaok/SaltAdmin/raw/master/static/images/ops_circle_qrcode.jpg)

#### QQ Group

**459457262**


#### KK Studio

http://studio.luxiaokc.com


## License

This project is under the MIT License. See the [LICENSE](http://git.luxiaok.com:82/xiaok/SaltAdmin/src/master/LICENSE) file for the full license text.