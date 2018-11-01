from os.path import join, dirname
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_config_file
from tornado.web import Application, RequestHandler, url


# 演示请求响应顺序

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('login.html')

    def post(self, *args, **kwargs):
        pass

class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        pass
    def post(self, *args, **kwargs):
        name = self.get_body_argument('name')
        password = self.get_body_argument('password')
        if name == 'abc' and password =='123':
            self.redirect('/blog')
        else:
            self.redirect('/')


class BlogHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('blog.html')
    def post(self, *args, **kwargs):
        pass


define('port',type=int,default=8888,multiple=False)
define('db',multiple=True,type=str,default=[])

parse_config_file('config')



app = Application([('/',IndexHandler),
                   ('/login',LoginHandler),
                   ('/blog',BlogHandler)
                    ],
                  template_path=join(dirname(__file__),'mytemp'))
server = HTTPServer(app)
server.listen(options.port)

# print("数据库参数:",options.db)

IOLoop.current().start()
