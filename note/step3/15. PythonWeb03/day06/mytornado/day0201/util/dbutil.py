import pymysql

from day0201.util.myutils import mymd5


class DBUtil:

    def __init__(self,**kwargs):
        #获取到与数据库的连接

        #直接使用用户传递的内容不太好
        #应该简单的提取
        host = kwargs.get('host','127.0.0.1')
        port =kwargs.get('port',3306)
        user = kwargs.get('user','root')
        password= kwargs.get('password','123456')
        database=kwargs.get('database','blogdb')
        charset = kwargs.get('charset','utf8')
        #把经过提取的内容作为参数传递给ｃｏｎｎｅｃｔ方法
        configs = dict(host=host,port=port,user=user,password=password,database=database,charset=charset)
        conn = pymysql.connect(**configs)

        #进而获取到结果集
        if conn:
            self.cursor = conn.cursor()
        else:
            raise Exception('数据库连接参数错误！')

    #注册用户
    def registUser(self,**kwargs):
        name = kwargs.get('name')
        password = kwargs.get('password')
        pwd = mymd5(password)
        city = kwargs.get('city')
        avatar_name = kwargs.get('avatar_name')

        sql='insert into tb_user(user_name,user_password,user_city,user_avatar) values(%s,%s,%s,%s)'
        params=(name,pwd,city,avatar_name)
        try:
            self.cursor.execute(sql,params)
            self.cursor.connection.commit()
        except Exception as e:
            #(1062,"Duplicat......")
            #raise Exception(e.__str__())
            info = e.__str__()
            # (1062
            m = info.split(',')[0]
            # errmsg = m[1:]
            errmsg = m.split('(')[1]
            err='数据库未知错误！'
            if errmsg == '1062':
                err = '用户名重复'
            raise Exception(err)



    #登录
    #　根据参数中提供的用户和密码
    #  去数据库tb_user表中查询是否有匹配的数据记录
    #  如果有，就返回Ｔｒｕｅ，否则Ｆａｌｓｅ
    def isloginsuccess(self,name,password):

        sql = 'select count(*) from tb_user where user_name=%s and user_password=%s'

        pwd = mymd5(password)

        params = (name,pwd)

        self.cursor.execute(sql,params)

        result = self.cursor.fetchone()

        if result[0]:
            return True
        else:
            return False

    #判定某个用户是否存在
    def hasUser(self,username):
        #利用ｕｓｅｒｎａｍｅ去tb_user表查询
        # return True / False
        sql = 'select count(*) from tb_user where user_name = %s'
        params=(username,)
        self.cursor.execute(sql,params)
        result = self.cursor.fetchone()#(xx,)
        # Ｔｒｕｅ　该用户名已经存在
        # False　该用户名不存在
        if result[0]:
            return True
        else:
            return False

    #根据用户名去tb_user中查找对应的头像文件名称
    def findAvatar(self,username):
        sql='select user_avatar from tb_user where user_name = %s'
        params=(username,)
        self.cursor.execute(sql,params)
        result = self.cursor.fetchone()#(xxx,)
        if result[0]:
            return result[0]
        else:
            return None
