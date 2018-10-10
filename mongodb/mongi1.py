from pymongo import MongoClient,IndexModel

conn = MongoClient('localhost',27017)

db = conn.stu

my_set = db.class4


##索引操作
#
##index = my_set.ensure_index('name')
#
#index = my_set.ensure_index([('name',1),('King',1)])
#
##print(index)

##先创建索引对象
#index1 = IndexModel([('name',1),('King',-1)])
#index2 = IndexNodel([('king_name',1)])
#
##通过create_indexes生成索引
#indexes = my_set.create_indexes([index1,index2])

##print(indexes)


#index = my_set.ensure_index('name', unique=True,sparse=True)
#
#for i in my_set.list_indexes():
#    print(i)
#
#
#my_set.drop_index('name_1_King_-1')
#for i in my_set.list_indexes():
#    print(i)
#
#
#
#my_set.drop_indexes()
#for i in my_set.list_indexes():
#    print(i)
#



##-------聚合操作--------##


l = [{'$group':{'_id':'$King','count':{'$sum':1}}},\
                {'$match':{'count':{'$gt':1}}}]

cursor = my_set.aggregate(l)
for i in cursor:
    print(i)



