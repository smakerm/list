import random
import time
from tornado.web import RequestHandler

from day4.myhandlers.myrequesthandler import MyRequestHandler
from day4.util.mysession import MySession


class IndexHandler(MyRequestHandler):
    def get(self, *args, **kwargs):
        # msg = ''
        # s = self.get_query_argument('msg', None)
        # if s:
        #     msg = '用户名或密码错误'
        # self.render('login.html',result=msg)
        self.set_cookie('mycookie','hello_world',expires_days=10)

        islogin = self.session['islogin']
        if islogin:
            self.redirect('/blog')
        else:
            self.render('login.html')

    def post(self, *args, **kwargs):
        pass

class LoginHandler(MyRequestHandler):
    def get(self, *args, **kwargs):
        pass
    def post(self, *args, **kwargs):
        name = self.get_body_argument('name')
        password = self.get_body_argument('password')


        res = self.application.dbutil.isloginsuccess(name, password)
        if res:

            self.session['islogin'] = True

            self.redirect('/blog')
        else:
            self.redirect('/?msg=fail')


class registHandler(MyRequestHandler):
    def get(self, *args, **kwargs):

        info = self.get_cookie('mycookie')
        print(info)

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

            try:
                params = dict(name=name, password=password, city=city, avatar_name=avatar_name)
                self.application.dbutil.registUser(**params)
                self.redirect('/')
            except Exception as e:
                errmsg = e.args[0]
                # 错误信息为中文
                self.redirect('/regist?msg=%s'%errmsg)
        else:
            self.redirect('/regist?msg=fail')

class BlogHandler(MyRequestHandler):
    def myrande(self, a, b):
        return random.randint(a, b)
    def get(self, *args, **kwargs):

        session = MySession(self)
        islogin = session['islogin']
        if islogin:
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
        else:
            self.redirect('/')
    def post(self, *args, **kwargs):
        pass


class checkHandler(MyRequestHandler):
    def get(self, *args, **kwargs):
        pass
    def post(self, *args, **kwargs):
        username = self.get_body_argument('username', None)

        if self.application.dbutil.hasUser(username):
            result = {'msg' : 'no'}
        else:
            result = dict(msg='ok')
        return self.write(result)


class getAvatarHandler(MyRequestHandler):
    def post(self, *args, **kwargs):
        username = self.get_body_argument('username', None)
        avatar_name =  self.application.dbutil.getavatar(username)

        msg = dict(msg='ok',avatar_name=avatar_name)
        self.write(msg)

    def get(self, *args, **kwargs):
        pass