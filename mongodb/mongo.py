from pymongo import MongoClient
import pymongo


#创建mongo的连接对象

conn = MongoClient('localhost',27017)

#选择要连接的数据库

db = conn.stu  #   __getitem__     __setitem__
#db = conn['stu']

#选择要连接的集合

my_set = db.class4
#my_set = db['class4']

##------增---加--------##

#my_set.insert({'name':'张铁林','King':'乾隆'})
#my_set.insert([{'name':'陈道明','King':'康熙'},{'name':'张国立','King':'康熙'}])
#
#my_set.insert_many([{'name':'唐国强','King':'雍正'},{'name':'陈建斌','King':'雍正'}])
#my_set.insert_one({'name':'吴奇隆','King':'四爷'})
#
#my_set.save({'name':'孙中山','King':'民国'})
#

##------删---除--------##
#my_set.remove({'name':'张铁林'})
#my_set.remove({'name':'陈道明'},multi=False)
#
#my_set.remove()

##------查---找--------##


#cursor = my_set.find({},{'_id':0})
#for i in cursor:
#    print(i)
##my_set.find_one()
#
#cls = db.class3
#for i in cls.find({'age':{'$gt':20}}):
#    print(i['name'],'---',i['age'])
#
#
#cursor = my_set.find({},{'_id':0})
#print(cursor.count())
#for i in cursor.skip(2).limit(3):
#    print(i)
#
#
#cursor = my_set.find({},{'_id':0})
#for i in cursor.sort([('name',1)]):
#    print(i)
#
#
#cursor.next()


##------修---改--------##

my_set.update({'name':'吴奇隆'},{'$set':{'King':'老四'}})
print(my_set.find_one({'name':'吴奇隆'}))


my_set.update({'name':'郑少秋'},{'$set':{'King':'乾隆'}},upsert=True)

print(my_set.find_one({'name':'郑少秋'}))


my_set.update({'King':'康熙'},{'$set':{'King_name':'玄烨'}}\
                                ,upsert=False,multi=True)

print(my_set.find({'King':'康熙'}))


my_set.update_many({'King':'雍正'},{'$set':{'King_name':'胤禛'}})




##-------复合操作-------##







my_set.close()
