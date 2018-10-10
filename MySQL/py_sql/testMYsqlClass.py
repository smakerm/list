from MysqlClass import MysqlPython


#name = input()
#score = int(input())

#sql = "update t1 set score='%s' where name='%s'" %(score,name)
sql2 = "select * from t1 WHERE name = '1'"

sqlH = MysqlPython("127.0.0.1", 3306, "python", "root", "123456")
#sqlH.zhixing(sql)

data = sqlH.all(sql2)

print(type(data))

