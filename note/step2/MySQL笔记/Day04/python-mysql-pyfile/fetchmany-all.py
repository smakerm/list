import pymysql

db = pymysql.connect("localhost","root",\
    "123456","python",port=3306,charset="utf8")
cur = db.cursor()
sql_select = "select * from t1;"
cur.execute(sql_select)
print("select语句查出的记录个数为:",cur.rowcount)

# data = cur.fetchmany(2)
# print("fetchmany(2)的结果集为：")
# for i in data:
#     print(i)
# print()

# data2 = cur.fetchall()
# print("fetchall()的结果集为：")
# for i in data2:
#     print(i)

db.commit()
cur.close()
db.close()
