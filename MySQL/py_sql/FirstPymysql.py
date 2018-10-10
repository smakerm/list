import pymysql

# 连接数据库
db = pymysql.connect("127.0.0.1","root","123456",charset="utf8")


cur = db.cursor()

cur.execute("create database if not exists python;")

cur.execute("use python;")

cur.execute("create table if not exists t1(\
            id int primary key,\
            name varchar(20),\
            score tinyint unsigned);")

cur.execute("insert into t1 values\
            (1,'貂蝉',88),\
            (2,'赵子龙',100),\
            (3,'诸葛亮',86);")

db.commit()

cur.close()

db.close()
