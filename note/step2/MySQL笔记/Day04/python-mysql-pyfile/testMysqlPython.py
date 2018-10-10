from MysqlPython import MysqlPython

# update
name = input("请输入要修改的学生姓名：")
score = int(input("请输入该学生的新成绩："))
sql = "update t1 set score='%s' where name='%s'"\
       %(score,name)
sqlH = MysqlPython("localhost",3306,"python",\
       "root","123456")

sqlH.zhixing(sql)















