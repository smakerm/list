from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_config_file
from tornado.web import Application, RequestHandler


class IndexHandle(RequestHandler):
    def get(self, *args, **kwargs):
        with open('login.html','r') as f:
            html = f.read()
        self.write(html)
    def post(self, *args, **kwargs):
        name = self.get_body_argument('uname', None)
        password = self.get_body_argument('upwd', None)
        print(name, password)

        files = self.request.files
        avatar = files.get('uavatar')[0]
        filename = avatar.get('filename')
        data = avatar.get('body')
        with open('upload/%s'%filename,'wb') as f:
            f.write(data)
        # self.redirect(url)
        self.write("post OK")

define('port',default=8888,type=int, multiple=False)
parse_config_file('config')


app = Application([
                ('/',IndexHandle),
                ])

server = HTTPServer(app)
server.listen(options.port)
IOLoop.current().start()