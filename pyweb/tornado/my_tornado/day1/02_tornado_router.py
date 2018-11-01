import tornado
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_config_file
from tornado.web import Application, RequestHandler, url

# tornado 路由设置

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('hello tornado')
    def post(self, *args, **kwargs):
        pass


class JavaHandler(RequestHandler):
    def initialize(self, greeting, info):
        self.greeting = greeting
        self.info = info

    def get(self, *args, **kwargs):
        self.write(self.greeting + ',' + self.info)

    def post(self, *args, **kwargs):
        pass

# /python
# /python/day1
# /python/day1/basic

class PythonHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello python")
        self.write('<br>')
        self.write("<a href=%s>jump java</a>"%self.reverse_url('java_url'))
        self.write('<br>')
        day = kwargs.get('day','None')
        title = kwargs.get('title', None)
        if day:
            self.write('第几天: ' + day)
        if title:
            self.write('课程内容: ' + title)
    def post(self, *args, **kwargs):
        pass

define('port',type=int,default=8888,multiple=False)
define('db',multiple=True,type=str,default=[])

parse_config_file('config')



app = Application([('/',IndexHandler),
                   url('/java',JavaHandler,{'greeting':'你好','info':'加瓦'},name='java_url'),
                   ('/python',PythonHandler),
                   ('/python/(?P<day>day[0-9]+)',PythonHandler),
                   ('/python/(?P<day>[a-zA-Z0-9]+)/(?P<title>[a-zA-Z]+)',PythonHandler),
                ])
server = HTTPServer(app)
server.listen(options.port)

# print("数据库参数:",options.db)

IOLoop.current().start()
