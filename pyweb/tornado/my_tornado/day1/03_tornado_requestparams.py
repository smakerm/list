import tornado
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_config_file
from tornado.web import Application, RequestHandler, url

# tornado 获取请求参数

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):

        arg = self.get_query_argument('day', None)
        print('arg------>' , arg)
        args = self.get_query_arguments('day')
        print('args----->' ,args)
        self.write('hello tornado')
    def post(self, *args, **kwargs):
        arg = self.get_body_argument('day', None)
        print(arg)
        args = self.get_body_arguments('day')
        print(args)
        a = self.get_query_arguments('day')
        print(a)

        header = self.request.headers
        print(header)

        self.write("hello post")


class JavaHandler(RequestHandler):
    def initialize(self, greeting, info):
        self.greeting = greeting
        self.info = info

    def get(self, *args, **kwargs):
        self.write(self.greeting + ',' + self.info)

    def post(self, *args, **kwargs):
        pass

class PythonHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello python")
        self.write('<br>')
        self.write("<a href=%s>jump java</a>"%self.reverse_url('java_url'))
    def post(self, *args, **kwargs):
        pass

define('port',type=int,default=8888,multiple=False)
define('db',multiple=True,type=str,default=[])

parse_config_file('config')



app = Application([('/',IndexHandler),
                   url('/java',JavaHandler,{'greeting':'你好','info':'加瓦'},name='java_url'),
                   ('/python',PythonHandler)])
server = HTTPServer(app)
server.listen(options.port)

# print("数据库参数:",options.db)

IOLoop.current().start()