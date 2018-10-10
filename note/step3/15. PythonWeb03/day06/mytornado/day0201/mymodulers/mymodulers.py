from tornado.web import UIModule


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
            #msg = '服务器繁忙，稍后重试'
            info = q.split('=')[1]
            print('info---->',info)
            if info=='fail':
                msg = '注册信息不完整'
            else:
                msg = info
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
