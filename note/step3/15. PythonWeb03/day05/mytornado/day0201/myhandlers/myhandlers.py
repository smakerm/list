import random

import time
from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def initialize(self):
        print('initialize方法执行')
    #响应以ｇｅｔ方式发起的请求
    def get(self, *args, **kwargs):
        print('get方法执行')

        #　服务器给浏览器的响应内容
        self.render('login.html')

    #响应以post方式发起的请求
    def post(self, *args, **kwargs):
        pass

    def on_finish(self):
        print('on_finish方法执行')

class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        pass
    def post(self, *args, **kwargs):
        name = self.get_body_argument('name',None)
        password = self.get_body_argument('password',None)

        if self.application.dbutil.isloginsuccess(name,password):
            self.redirect('/blog')
        else:
            self.redirect('/?msg=fail')

class BlogHandler(RequestHandler):

    def my_rand(self,a,b):
        return random.randint(a,b)

    def get(self, *args, **kwargs):
        self.render('blog.html')
    def post(self, *args, **kwargs):
        pass

class RegistHandler(RequestHandler):

    def get(self, *args, **kwargs):

        self.render('regist.html')

    def post(self, *args, **kwargs):
        #收集用户提交的注册信息并写入数据库，完成新用户注册
        name = self.get_body_argument('name',None)
        password = self.get_body_argument('password',None)
        city = self.get_body_argument('city',None)
        #判断用户提交必要信息是否完整
        if name and password and city:
            #用户头像文件保存在服务器磁盘上对应文件的名称
            avatar_name = None
            #用户有没有上传头像
            files = self.request.files
            avatar = files.get('avatar',None)
            if avatar:
                #用户上传了头像文件
                #将用户上传的头像文件保存
                avatar_file = avatar[0]
                filename = avatar_file.get('filename')
                body = avatar_file.get('body')
                filename = str(time.time()) + filename
                writer = open('mystatics/images/%s'%filename,'wb')
                writer.write(body)
                writer.close()
                #将保存文件的名称赋值给avatar_name
                avatar_name = filename

            #将用户信息写入数据库tb_user数据表

            try:
                #执行新增操作时，有可能出现用户名重复的情况
                #导致数据库扔出异常
                params = dict(name=name,password=password,city=city,avatar_name=avatar_name)
                self.application.dbutil.registUser(**params)
                self.redirect('/')

            except Exception as e:
                #打印异常信息
                print(e)
                errmsg = e.__str__()
                self.redirect('/regist?msg=%s' % errmsg)


        else:
            self.redirect('/regist?msg=fail')


class CheckHandler(RequestHandler):
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):

        username = self.get_body_argument('username',None)
        print('获取到的username:----->',username)

        #利用ｄｂｕｔｉｌ去根据ｕｓｅｒｎａｍｅ查询
        #tb_user表中是否已有该用户名
        if self.application.dbutil.hasUser(username):
            result = dict(msg='ok')
        else:
            result = dict(msg='no_ok')



        self.write(result)
