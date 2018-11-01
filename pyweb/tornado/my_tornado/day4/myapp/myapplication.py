from tornado.web import Application

from day4.util.dbutil import DBUtil


class MyApplication(Application):
    def __init__(self, routers, tp ,sp ,um):
        super().__init__(routers, template_path=tp,static_path=sp,ui_modules=um)
        self.dbutil = DBUtil()