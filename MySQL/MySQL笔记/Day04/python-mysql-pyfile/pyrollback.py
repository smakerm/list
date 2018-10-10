import pymysql

db = pymysql.connect("localhost","root",\
    "123456","db3",charset="utf8")
cur = db.cursor()

try:
    cur.execute("update CCB set money=95000 \
                where name='转钱';")
    cur.execute("update ICBC  money=7000 \
                where name='借钱';")
    db.commit()
    print("ok")
except Exception as e:
    db.rollback()
    print("出现错误,已经回滚")

cur.close()
db.close()