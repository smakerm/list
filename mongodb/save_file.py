from pymongo import MongoClient
import bson.binary

conn = MongoClient('localhost',27017)

db = conn.savefile

my_set = db.image


###存储文件
##file = './123.jpg'
##
##
##f = open(file,'rb')
##
###将读取的二进制字节流转换为bson格式的二进制字串
##dic = dict(content = bson.binary.Binary(f.read()),filename = 'img.jpg')
##
###插入文档
##my_set.save(dic)
##

#提取文件

##data = my_set.find_one({'filename':'img.jpg'})
##
##with open('img.jpg','wb') as f:
##    f.write(data['content'])
##

#提取文件2
data = my_set.find({'filename':'img.jpg'})
for i in data:
    with open(i['filename'],'wb') as f:
        f.write(i['content'])


conn.close()
