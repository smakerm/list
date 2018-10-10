import pymysql

db = pymysql.connect("127.0.0.1","root","","db3",charset="utf8")

cur = db.cursor()


try:
    cur.excute()
    cur.excute()
    db.commit()
except Exception as e:
    print(e)
    db.rollback()


cur.close()
db.close()
