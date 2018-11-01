import hashlib
import random
from os.path import join, dirname

import time
from urllib.parse import unquote

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_config_file
from tornado.web import Application, RequestHandler, url, UIModule
import pymysql

from day4.myapp.myapplication import MyApplication
from day4.myconfig import myconfig
from day4.myhandlers.myhandlers import IndexHandler, LoginHandler, BlogHandler, registHandler, checkHandler, \
    getAvatarHandler
from day4.mymodules.mymodules import MyModule, MyBlogModule, MyRegistModule
from day4.util.dbutil import DBUtil
from day4.util.myutils import mymd5

# 演示请求响应顺序


app = MyApplication(
    [
        ('/',IndexHandler),
        ('/login',LoginHandler),
        ('/blog',BlogHandler),
        ('/regist',registHandler),
        ('/check',checkHandler),
        ('/get_avatar',getAvatarHandler)
    ],
    tp=join(dirname(__file__),'mytemp'),
    sp='mystatics',
    um={
        'mymodule': MyModule,
        'myblogmodule': MyBlogModule,
        'myregistmodule':MyRegistModule,
        })
server = HTTPServer(app)
server.listen(myconfig.configs['port'])

# print("数据库参数:",options.db)

IOLoop.current().start()
