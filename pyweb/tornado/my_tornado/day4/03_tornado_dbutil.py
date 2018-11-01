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

from day4.util.dbutil import DBUtil
from day4.util.myutils import mymd5

# 演示请求响应顺序


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # msg = ''
        # s = self.get_query_argument('msg', None)
        # if s:
        #     msg = '用户名或密码错误'
        # self.render('login.html',result=msg)
        self.render('login.html')

    def post(self, *args, **kwargs):
        pass

class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        pass
    def post(self, *args, **kwargs):
        name = self.get_body_argument('name')
        password = self.get_body_argument('password')

        dbutil = DBUtil()
        res = dbutil.isloginsuccess(name, password)
        if res:
            self.redirect('/blog')
        else:
            self.redirect('/?msg=fail')


class registHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('regist.html')
    def post(self, *args, **kwargs):
        name = self.get_body_argument('name', '')
        password = self.get_body_argument('password', '')
        city = self.get_body_argument('city', '')
        if name and password and city:
            avatar_name = None
            files = self.request.files
            avatar = files.get('avatar', None)
            if avatar:
                avatar_file = avatar[0]
                filename = avatar_file.get('filename')
                body = avatar_file.get('body')
                filename = str(time.time()) + filename
                with open('mystatics/images/%s'%filename, 'wb') as f:
                    f.write(body)
                avatar_name = filename

            dbutil = DBUtil()

            try:
                params = dict(name=name, password=password, city=city, avatar_name=avatar_name)
                dbutil.registUser(**params)
                self.redirect('/')
            except Exception as e:
                errmsg = e.args[0]
                # 错误信息为中文
                self.redirect('/regist?msg=%s'%errmsg)
        else:
            self.redirect('/regist?msg=fail')

class BlogHandler(RequestHandler):
    def myrande(self, a, b):
        return random.randint(a, b)
    def get(self, *args, **kwargs):
        self.render('blog.html',myrand=self.myrande,\
                    blogs=[
                        {
                            'title':'第一篇博客',
                            'tag':['星座','运势'],
                            'content':'好长好长的正文',
                            'author':'默默人',
                            'avatar':'a.jpg',
                            'comment':0,
                        },
                        {
                            'title': '第二篇博客',
                            'tag': ['网络', '技术'],
                            'content': '好长好长的正文',
                            'author': '某某人',
                            'avatar': None,
                            'comment': 430,
                        },
                    ])
    def post(self, *args, **kwargs):
        pass


class MyModule(UIModule):
    def render(self, *args, **kwargs):
        msg = ''
        # uri = self.request.uri
        query = self.request.query
        if query:
            msg = '用户名或密码错误'
        return self.render_string('module/module_login.html',result=msg)


class MyBlogModule(UIModule):
    def render(self, *args, **kwargs):
        blogs = [
            {
                'title': '第一篇博客',
                'tag': ['星座', '运势'],
                'content': '好长好长的正文',
                'author': '默默人',
                'avatar': 'a.jpg',
                'comment': 0,
            },
            {
                'title': '第二篇博客',
                'tag': ['网络', '技术'],
                'content': '好长好长的正文',
                'author': '某某人',
                'avatar': None,
                'comment': 430,
            },
        ]
        return self.render_string('module/module_blog.html',blogs=blogs)


class MyRegistModule(UIModule):
    def render(self, *args, **kwargs):
        msg = ''
        query = self.request.query
        if query:
            msg = '服务器繁忙,稍后重试'
            info = query.split('=')[1]
            if info == 'fail':
                msg = '注册信息不完整'
            else:
                # 将url进行解码，显示在网页中
                msg = unquote(info)

        return self.render_string('module/module_regist.html', result=msg)



define('port',type=int,default=8888,multiple=False)
define('db',multiple=True,type=str,default=[])

parse_config_file('config')



app = Application([('/',IndexHandler),
                   ('/login',LoginHandler),
                   ('/blog',BlogHandler),
                   ('/regist',registHandler),
                    ],
                  template_path=join(dirname(__file__),'mytemp'),
                  static_path='mystatics',
                  ui_modules={'mymodule': MyModule,
                              'myblogmodule': MyBlogModule,
                              'myregistmodule':MyRegistModule,
                              })
server = HTTPServer(app)
server.listen(options.port)

# print("数据库参数:",options.db)

IOLoop.current().start()
