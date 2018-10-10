
# ｔｏｒｎａｄｏ演示通过继承Ａｐｐｌｉｃａｔｉｏｎ类添加自定义属性
# 每次使用ｄｂｕｔｉｌ操作数据表时，不用反复构建对象
import hashlib
import random
import pymysql
import time

import tornado
from os.path import join, dirname
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_config_file
from tornado.web import Application, RequestHandler, UIModule
#代码移动ALT+SHIFT＋方向
from day0201.myapp.myapplication import MyApplication
from day0201.myconfig import myconfig
from day0201.myhandlers.myhandlers import IndexHandler, LoginHandler, BlogHandler, RegistHandler, CheckHandler
from day0201.mymodulers.mymodulers import MyModule, MyBlogModule, MyRegistModule
from day0201.util.dbutil import DBUtil
from day0201.util.myutils import mymd5

#创建Ａｐｐｌｉｃａｔｉｏｎ对象，进行若干个对服务器的设置
#例如：路由列表，模板路径，静态资源路径等
app = MyApplication([('/',IndexHandler),
                   ('/login',LoginHandler),
                   ('/blog',BlogHandler),
                   ('/regist',RegistHandler),
                     ('/check',CheckHandler)],
                  tp=join(dirname(__file__),'mytemplate'),
                  sp=join(dirname(__file__),'mystatics'),
                  um={'mymodule':MyModule,
                              'myblogmodule':MyBlogModule,
                              'myregistmodule':MyRegistModule})
#创建服务器程序
server = HTTPServer(app)
#服务器监听某个端口(建议使用１００００以上的端口)
server.listen(myconfig.configs['port'])#10000
#启动服务器（在当前进程中启动服务器）
IOLoop.current().start()


