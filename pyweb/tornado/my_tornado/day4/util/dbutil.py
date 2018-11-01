import pymysql
import time

from day4.util.myutils import mymd5


class DBUtil:
    def __init__(self, **kwargs):

        host = kwargs.get('host', '127.0.0.1')
        port = kwargs.get('port', 3306)
        user = kwargs.get('user', 'root')
        password = kwargs.get('password','123456')
        database = kwargs.get('database', 'blogdb')
        charset = kwargs.get('charset', 'utf8')
        configs = dict(host=host,port=port,user=user,password=password,database=database,charset=charset)


        conn = pymysql.connect(**configs)

        if conn:
            self.cursor = conn.cursor()
        else:
            raise Exception('数据库连接参数错误！')

    def registUser(self, **kwargs):
        name = kwargs.get('name')
        password = kwargs.get('password')
        city = kwargs.get('city')
        avatar_name = kwargs.get('avatar_name')

        # if avatar:
        #     avatar_file = avatar[0]
        #     filename = avatar_file.get('filename')
        #     body = avatar_file.get('body')
        #     filename = str(time.time()) + filename
        #     with open('mystatics/images/%s' % filename, 'wb') as f:
        #         f.write(body)
        #     avatar_name = filename

        sql = 'insert into tb_user(user_name, user_password, user_city, user_avatar) VALUES (%s,%s,%s,%s)'

        pwd = mymd5(password)

        params = (name, pwd, city, avatar_name)
        try:
            self.cursor.execute(sql, params)
            self.cursor.connection.commit()
        except Exception as e:
            errcode = str(e.args[0])
            err = '数据库未知错误'
            if errcode == '1062':
                err = '用户名已存在'
            raise Exception(err)



    def isloginsuccess(self, name, password):

        sql = 'select count(*) from tb_user WHERE user_name=%s and user_password=%s'
        pwd = mymd5(password)
        params = (name, pwd)

        self.cursor.execute(sql, params)
        result = self.cursor.fetchone()

        if result[0]:
            return True
        else:
            return False

    def hasUser(self,username):
        sql = 'select count(*) from tb_user where user_name=%s'
        params = (username,)

        self.cursor.execute(sql, params)
        result = self.cursor.fetchone()
        if result[0]:
            return True
        else:
            return False

    def getavatar(self, username):
        sql = 'select user_avatar from tb_user where user_name=%s'
        params = (username,)
        self.cursor.execute(sql, params)
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None



