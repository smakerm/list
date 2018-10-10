from pymongo import MongoClient

#和pymongo文件绑定
import gridfs


conn = MongoClient('localhost',27017)
db = conn.grid

#获取gridfs对象

fs = gridfs.GridFS(db)

files = fs.find()

#print(files)
#print(files.count())

##files为可迭代对象，每个迭代值代表一个存入文件的对象
##通过对象的属性可获得文件信息
#for file in files:
#    print(file.filename)

for file in files:
    filename = './cc/' + file.filename
    with open(filename,'wb') as f:
        while True:
            data = file.read(64)
            if not data:
                break
            f.write(data)


conn.close()
