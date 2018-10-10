#演示tornado页面间的跳转

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler

#模块级别的变量　访问（读/写）
# 被遮蔽住了
IS_SUCCESS = True

class IndexHandler(RequestHandler):

    def get(self, *args, **kwargs):

        html='<form method=post action=/login enctype=multipart/form-data>' \
             '<input type=text name=name><br><br>' \
             '<input type=password name=password><br><br>' \
             '<input type=submit value=提交>&nbsp;&nbsp;&nbsp;' \
             '<input type=reset value=重置>' \
             '</form>'

        self.write(html)

        # if not IS_SUCCESS:
        #     self.write('<br><br>')
        #     self.write('<span style=color:red;font-weight=bold;>用户名或密码错误！</span>')

        msg = self.get_query_argument('msg',None)
        if msg:
            self.write('<br><br>')
            self.write('<span style=color:red;font-weight=bold;>用户名或密码错误！</span>')

    def post(self, *args, **kwargs):
        pass

class LoginHandler(RequestHandler):
    global IS_SUCCESS

    def get(self, *args, **kwargs):
        pass
    def post(self, *args, **kwargs):
        name = self.get_body_argument('name')
        password = self.get_body_argument('password')
        print('用户名: ',name,' , 密码:', password)
        if name=='abc' and password=='123':
            #如果输入的用户名为ａｂｃ，密码是１２３
            #则跳转到博客的页面(127.0.0.1:9999/blog)
            #IS_SUCCESS = True
            self.redirect('/blog')
        else:
            #否则重新输入用户名和密码再次进行登录
            #IS_SUCCESS = False
            #self.redirect('/')
            self.redirect('/?msg=fail')


class BlogHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('welcome blog')
    def post(self, *args, **kwargs):
        pass

define('port',default=8888,type=int,multiple=False)
parse_config_file('config')
app = Application([('/',IndexHandler),
                   ('/login',LoginHandler),
                   ('/blog',BlogHandler)])
server = HTTPServer(app)
server.listen(options.port)
IOLoop.current().start()