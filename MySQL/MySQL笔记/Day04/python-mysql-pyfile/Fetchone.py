import pymysql

db = pymysql.connect("localhost","root",
              "123456","python",charset="utf8")
cur = db.cursor()

sql_select = "select * from t1;"
cur.execute(sql_select)

# data = cur.fetchone()
# print("fetchone的结果为：",data)

db.commit()
cur.close()
db.close()



