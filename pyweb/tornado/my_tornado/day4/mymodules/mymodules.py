from urllib.parse import unquote

from tornado.web import UIModule


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

