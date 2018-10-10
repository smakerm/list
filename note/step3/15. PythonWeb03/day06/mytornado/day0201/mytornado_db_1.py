
# ｔｏｒｎａｄｏ演示ｐｙｔｈｏｎ操作数据库
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
from day0201.util.dbutil import DBUtil
from day0201.util.myutils import mymd5


# 用来响应用户请求


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
        #利用用户输入的用户名和密码
        #通过ｐｙｍｙｓｑｌ到数据库的tb_user数据表中进行查询
        #1. 利用ｐｙｍｙｓｑｌ建立与数据库的连接
        connect = pymysql.connect(host='127.0.0.1',
                                  port=3306,
                                  user='root',
                                  password='123456',
                                  database='blogdb',
                                  charset='utf8')
        print('connect---->',connect)
        #2. 通过连接获取一个结果集
        cursor = connect.cursor()
        #3. 利用结果集发送ＳＱＬ语句操作数据库
        sql = 'select count(*) ' \
              'from tb_user ' \
              'where user_name=%s ' \
              'and user_password=%s'

        #对用户输入的登录密码进行md5转码
        # md = hashlib.md5()
        # md.update(password.encode('utf8'))
        # pwd = md.hexdigest()

        pwd = mymd5(password)

        param = (name,pwd)
        # where user_name="a\" or 1=1 or \("\1\"=\"1" and user_password="1\"\) or \"1\"=\"1"


        print ('sql:',sql)
        #cursor.execute(sql)
        cursor.execute(sql,param)
        #4. 利用结果集获取数据库返回的内容
        #result = cursor.fetchall()#((数据记录１),(数据记录２),...)
        result = cursor.fetchone()#(数据记录１)
        print('result----->',result)
        if result[0]:
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

            configs = {
                'host':'127.0.01',
                'port':3306,
                'user':'root',
                'password':'123456',
                'database':'blogdb',
                'charset':'utf8'
            }
            # **configs是将字典中的键值对自动拆分为关键字形式传参
            connect = pymysql.connect(**configs)
            cursor = connect.cursor()
            sql = 'insert into tb_user(user_name,user_password,user_city,user_avatar) values (%s,%s,%s,%s)'

            #对用户直接输入的密码进行md5的转码
            #123 ---> md5格式字符串
            #md = hashlib.md5()
            #md.update(password.encode('utf8'))
            #ｐｗｄ就是将ｐａｓｓｗｏｒｄ进行md5转码后的结果
            #pwd = md.hexdigest()

            pwd = mymd5(password)

            params = (name,pwd,city,avatar_name)
            try:
                #执行新增操作时，有可能出现用户名重复的情况
                #导致数据库扔出异常
                cursor.execute(sql,params)
                #进行提交，将内容真正写入数据表
                #connect.commit()
                cursor.connection.commit()

                self.redirect('/')

            except Exception as e:
                #打印异常信息
                print(e)
                #print(e.__str__())
                #print(type(e.__str__()))
                info = e.__str__()
                #(1062
                m = info.split(',')[0]
                #errmsg = m[1:]
                errmsg = m.split('(')[1]
                #/regist?msg=1062
                self.redirect('/regist?msg=%s' % errmsg)


        else:
            self.redirect('/regist?msg=fail')

class MyModule(UIModule):
    def render(self, *args, **kwargs):
        msg=''
        #uri = self.request.uri
        #print('uri:---->',uri)
        query = self.request.query
        print('query:--->',query)
        if query:
            msg='用户名或密码错误！'

        return self.render_string('module/module_login.html',result=msg)

class MyRegistModule(UIModule):
    def render(self, *args, **kwargs):
        msg = ''
        q = self.request.query
        if q:
            #有问题　msg = fail  msg=1062
            msg = '服务器繁忙，稍后重试'
            info = q.split('=')[1]
            if info=='fail':
                msg = '注册信息不完整'
            if info=='1062':
                msg = '用户名重复！'

        return self.render_string('module/module_regist.html',result=msg)

class MyBlogModule(UIModule):
    def render(self, *args, **kwargs):
        return self.render_string('module/module_blog.html',blogs=[{'title':'第一篇博客',
                            'tag':['情感','男女','星座'],
                            'content':'好长好长好长的正文',
                            'author':'某某人',
                            'avatar':'a.jpg',
                            'comment':45},

                           {'title':'第二篇博客',
                            'tag':['技术','达内'],
                            'content':'学好python找我就对了',
                            'author':'大旭旭',
                            'avatar':None,
                            'comment':0}])

#定义一个变量，用来代表端口号
define('port',type=int,default=8888,multiple=False)
#定义一个变量，用来代表数据库的连接信息(用户名，密码，端口号，数据库名称)
define('db',multiple=True,type=str,default=[])
#从指定的配置文件中，读取ｐｏｒｔ的内容
parse_config_file('config')

#创建Ａｐｐｌｉｃａｔｉｏｎ对象，进行若干个对服务器的设置
#例如：路由列表，模板路径，静态资源路径等
app = Application([('/',IndexHandler),
                   ('/login',LoginHandler),
                   ('/blog',BlogHandler),
                   ('/regist',RegistHandler)],
                  template_path=join(dirname(__file__),'mytemplate'),
                  static_path=join(dirname(__file__),'mystatics'),
                  ui_modules={'mymodule':MyModule,
                              'myblogmodule':MyBlogModule,
                              'myregistmodule':MyRegistModule})
#创建服务器程序
server = HTTPServer(app)
#服务器监听某个端口(建议使用１００００以上的端口)
server.listen(options.port)#10000
#打印获得的数据库参数
print('数据库参数：',options.db)
#启动服务器（在当前进程中启动服务器）
IOLoop.current().start()


