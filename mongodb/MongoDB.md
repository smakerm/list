##**MongoDB**

数据库优点：
	数据组织结构化
	冗余度小
	容易扩充
	查找效率高
	方便使用程序自动处理
缺点：
	需要使用sql语句等特定语句处理，相对比较复杂

数据库三范式：
1. 1NF 每一列都是不可分割的原子数据项
2. 2NF 要求实体的属性完全依赖于主关键字。所谓完全依赖是指不能存在仅依赖主关键字一部分的属性
3. 3NF 任何非主属性不依赖于其它非主属性（在2NF基础上消除传递依赖）


###**关系型数据库：采用关系模型来组织数据结构的数据库**

####优点：
1. 容易理解，类似表格模型
2. 使用方便，都是通过sql语句进行操作，sql语句是非常成熟的
3. 易于维护，完整性好，数据一致性高，降低了冗余
4. 技术成熟，可以使用外连接等比较复杂的操作
####缺点：
1. 不能很好的满足高并发的需求，每次操作需要sql语句需要解析
2. 针对海量数据的瞬间爆发在读写上显得不足，关系型数据库内部每一步操作为了保证原子性都会加锁
3. 数据一致性较高，在处理某些数据情况是浪费资源
4. 数据库扩展比非关系型数据库要更复杂

###**非关系型数据库**
####优点：
1. 高并发，大数据下读写能力强
2. 支持分布式，容易扩展
3. 弱化了数据结构，降低了数据的一致性

####缺点：
1. 没有join等复杂的操作
2. 通用性差
3. 操作灵活即容易混乱

####nosql的使用情况：
1. 数据模型简单灵活，一致性差
2. 对数据库的并发处理要求高
3. 数据库设计师无法准确估量大小，后期可能需要扩展
4. 给定的数据关系比较容易建立起键值模型

####Noslq的分类：
1. 键值型数据库
	Redis		oracle BDB		Tokyo
2. 列存储数据库
	HBase

3. 文档型数据库
	MongoDB	CouchDB

4. 图形数据库




###**MongoDB**

1. 是一个文档型非关系数据库
2. 由C++编写的数据库
3. 支持丰富的查询操作
4. 支持众多编程语言的接口
5. 使用简单，便于部署
6. 数据格式丰富
7. 支持分布式扩展

mongodb 端口号 27017
设置
mongod --dbpath path
mongod --port port

数据库的命名规则：
1. 原则上是满足以下几条的任意UTF-8格式的字符串
2. 不能是''（空）字符
3. 不能含有空格' ' 点'.' '/' '\' '\0'
4. 习惯上全部使用小写
5. 不应超过64字节
6. 不能使用adimin local config 
集合的命名规则：
1. 不能是空字符串
2. 不能含有'\0'
3. 不能以system.开头这是系统集合的保留前缀
4. 集合不能和保留字重名，不要包含$




admin: 存储用户权限
local: 不会被复制，只能由于本机操作
config:分片处理时存储分片信息

####数据类型：
类型	|	说明
-----------|--------------	
整型	|	32位
布尔型	|	True False
浮点型	|	存储小数
Arrays	|	列表数组
Timestamp	|	时间戳
Date	|	时间日期
Object	|	内部文档
null	|	空值	
sumbol	|	特殊字符
Binary data	|	二进制数据
code	|	代码js	
regex	|	正则表达式
ObjectID	|	ObjectID字串

ObjiectID:	系统自动为每个文档生成的不重复的主键
				键名称	>	id
				值		>	ObjectID("24位16进制数")
8 文档创建事件		6 机器ID		4 进程ID		6 计数器

null	
1. 某个域没有值却存在则可以设置为null
2. 表示某个域不存在也能够进行匹配

文档类型数据：
`db.book.find({"Python.title":"Python web"},{_id:0})`
*外部文档的域引用内部文档的域通过 "." 的方法逐层引用，在使用时需要加引号*
`db.book.update({"Python.title":"Python web"},{$set:{"Python.price":40.8}})`
`db.class1.find({"hobby.0":"song"},{_id:0})`

文档有序性的体现
`db.class1.find({},{_id:0})[2]`




mongodb 存储数据库的一些概念
|mysql|mongo|含义|
|---|---|---|
|database|collection|表/集合|
|column|field|子段/域|
|row|document|记录/文档|
|index|index|索引|


操作|语句
---|---
创建数据库|`use databasename`
查看数据库|`show dbs`
备份数据库|`mongodump -h dbhost -o dbdir`
恢复数据库|`mongorestore -h <hostname>:<port> -d dbname <path>`
检测数据库|`mongostat`
检测每个数据库的读写时长|`mongotop`
删除数据库|`db.dropDatabase()`
```
use实际功能表示选择使用数据库，如果选择一个不存在的数据库，则当向这个数据库插入数据时，数据库会自动创建
db 表示当前正在使用的数据库。默认表示test数据库
```


参数		|	内容
---			|---
insert		|	每秒插入次数
query 		|	每秒查询次数
update		|	每秒更新次数
delete		|	每秒删除次数
getmore	|	
command	|	每秒运行命令次数
dirty		|	
used		|	使用率
flushes	|
vsize		|	使用虚拟内存情况
res			|	使用物理内存情况
qrw			|
arw			|
net_in		|	网络输入
net_out	|	网络输出
conn		|	连接数
time		|	时间


操作|命令
------|------
创建集合|`db.createCollection(collection_name)`<br>`db.collection.insert({})`
查看集合|`show tables`或`show collections`
删除集合|`db.collection.drop()`
修改集合名称|`db.collection_name.renameCollection("NewName")`

文档（bson）
在mongodb中数据的组建形式
由键值组成，类似python中的字典

文档中 键的命名规则
1. utf-8 格式的字符串
2. 不能有\0 不能为空 （习惯上不用.和$）
3. 以_开头的很多都是保留的键，所以一般不用_开头
注意：
	文档中的键值对是有序的
	文档中的值指的就是文档支持的数据类型
	mongodb中区分大小写


集合设计原则
1. 同一类文档存在一个集合中
2. 集合中尽量存储域和文档格式相近的文档
3. 集合中可以存在文档数据的差异

操作		|	命令
-------		|	-------
插入文档	|	`db.collection_name.insert([{},{},{}])`
插入文档2	|	`db.collection_name.save()`
查找		|	`db.collection_name.find()`<br>`db.collection_name.findOne()`
删除文档	|	`db.collection_name.remove(query,justOne)`
更新文档	|	`db.collcetion_name.update(query,updata,upsert,multi)`
查找内部文档|	`db.book.find({"Python.title":"Python web"},{_id:0})`

###**查找**
**find(query,field)**
功能：	查找所有符合筛选要求的文档
参数：
	query:	筛选条件	相当于where子句
	field:	展示的域	0 表示不展示该域	1 表示展示该域

返回值：	返回所有符合要求的文档
*field:	选择要展示的域*
1. 以键值对的形式给每个域赋值0，1表示是否要显示该域
2. 如果给域设置为0，其他域自动为1，如果给某个域设置为1，则其他的自动为0。两者不能混用
3. _id 比较特殊，默认为1，如果不想显示则设置为0。_id为0时其他的域可以为1.
4. 如果不写该参数，则表示显示所有的域

*query*
1. 以键值的方式确定查找条件
2. 如果不写这个参数则表示查找所有文档

**findOne()**
功能：	查找符合条件的第一条文档
参数：	同find
返回值：	返回查找到的文档



* *_id为系统定义的主键值，如果使用系统值则保证不重复，如果自定义值即会覆盖系统值，但是自己也不能让该域重复*
* *save 如果不添加\_id域时同insert，如果添加_id域，该域不存在时则正常插入，如果存在则修改原数据.save 不能插入多条文档*


比较运算符：
语法|	含义
------|	-----
$eq	|	等于
$lt	|	小于
$lte|	小于等于
$gt	|	大于
$gte|	大于等于
$ne	|	不等于
$in	|	in
$nin|	not in

`db.class3.find({age:{$gt:24}},{_id:0})`
`db.class3.find({age:{$in:[24,27]}},{_id:0})`

逻辑运算符
$and	and
$or		or
$not	not
$nor	not or


`db.class3.find({$and:[{age:27},{sex:'m'}]},{_id:0})`
`db.class3.find({age:{$gt:25,$lt:30}},{_id:0})`
`db.class3.find({$or:[{age:27},{sex:'f'}]},{_iddb.class.insert({[name:'xiaohong',age:10,sex:'f',hobby:['draw','song','dance']],[name:"xiaoming",age:5,sex:'m',hobby:['football','song']],[name:"xiangwang",age:3,sex:'m',hobby:["draw","dance"]]})
:0})`
`db.class3.find({age:{$not:{$eq:24}}},{_id:0})`
`db.class3.find({$nor:[{age:18},{sex:'m'}]},{_id:0})`
`db.class3.find({$or:[{age:{$lt:20}},{name:"arong",sex:'f'}]},{_id:0})`

数组查找：
查找类型|语句
---|---
查找hobby中包含song的	|	`db.class1.find({hobby:'song'},{_id:0})`
查找数组中包含多项的文档	|	`db.class1.find({hobby:{$all:['speak','not']}},{_id:0})`
查找数组中项数为制定个数的文档	|	`db.class1.find({hobby:{$size:2}},{_id:0})`
显示数组中的前几项			|	`db.class1.find({},{_id:0,hobby:{$slice:-1}})`
`$slice 支持类似python中的切片操作`


其他查找方法：

$exists	|	判断一个域是否存在		|	`db.class3.find({sex:{$exists:true}},{_id:0})`
$mod		|	查找age被2整余1的文档	|	`db.class3.find({age:{$mod:[2,1]}},{_id:0})`
$type		|	查找值为指定数据类型的文档	|`db.class3.find({age:{$type:1}},{_id:0})`

distinct	|	查看一个集合中某个域的值所覆盖的范围	|	`db.class1.distinct('hobby')`
pretty()	|	将查询结果格式化显示	|	`db.class1.find({},{}).pretty()`
limit(n)	|	查询结果显示前N个文档	|	`db.class1.find({},{}).limit(3)`
skip(n)	|	跳过前N条显示			|	`db.class1.find({},{}).skip(3)`
count()	|	对查询记录进行统计		|	`db.class3.find({age:24},{_id:0}).count()`
sort()		|	按照制定的字段进行排序	|	`db.class3.find({},{_id:0}).sort({age:1})`
explain()	|	显示详细的查找信息		|	``


sort()
参数：	键值对	1 按照升序 ，-1降序
复合排序：
db.class3.find({},{_id:0}).sort({age:-1},{name:1})


1. 默认在query中逗号分割的多个条件即为i逻辑与关系
2. 函数可以联合使用



###**更新**

`db.collcetion_name.update(query,updata,upsert,multi)`

功能：	更改一个文档数据
参数：	query	
		update	：	将数据更新为什么，相当于set，需要配合修改器操作符来使用
		upsert：	bool值，默认为false，表示当定位的文档不存在则无法修改。
					如果为true，表示如果定位的文档不存在，则插入这条文档
		multi	：	bool，默认为false，如果query匹配的文档有多条，则只修改第一条
					如果设置为true，则修改所有匹配到的文档


修改器：	将数据修改为什么


$set 修改一个值 为文档增加一个域
$unset		删除一个域
$rename	修改一个域的名称
$inc		对某个域的值进行加减修改		`db.class3.update({name:"xiang"},{$inc:{age:1}})`
$mul		对某个域的值进行乘法修改		`db.class3.update({name:"xiaohong"},{$mul:{age:2}})`
$min		设定最小值，如果query到的文档指定域小于min设定则不做修改，如果大于指定的min值则改为min值		`db.class3.update({name:"消亡"},{$min:{age:26}})`
$max		设定最大值，如果query到的文档指定域大于max设定则不做修改，如果小于指定的max值则改为max值		`db.class3.update({},{$max:{age:22}},false,true)`

####**数组修改器**
$push		增加一项		`db.class1.update({name:"Lucy"},{$push:{hobby:"computer"}})`
$pushAll	增加多项("3.6取消")		`db.class1.update({name:"Jam"},{$pushAll:{hobby:["Python","html"]}})`
$each		每一项
$pull		从数组中删除一个元素		`db.class1.update({name:"Tom"},{$pull:{hobby:'chui'}})`
$pullAll	从数组中删除多个元素
$pop		从数组两端弹出元素			`db.class1.update({name:"Jam"},{$pop:{hobby:1}})`
$addToSet	向数组中无重复添加一个元素	`db.class1.update({name:"Tom"},{$addToSet:{hobby:"KongFu"}})`


###**索引**

指的是建立指定的键值及所在文档中的存储位置对照关系清单。使用索引可以方便我们快速查找，减少便利次数，提高效率

创建索引：	
ensureIndex()
功能：创建索引
参数：提供索引的类别选项

根据name域创建索引	`db.class1.ensureIndex({name:1})`	
查看当前集合索引		`db.class1.getIndexes()`	
创建符合索引（同时根据多个域创建索引）	`db.class3.getIndexes({name:1,age:-1})`
删除索引				`db.class1.dropIndex({name:1})`
删除除_id外的全部索引	`db.class3.dropIndexes()`

索引类型：
1. 数组索引：如果对某个数组域创建索引，则对数组中的每个值创建索引，则对数据中的每个值均创建了索引。通过数组中单个查询也会提高效率
2. 子文档索引：如果某个域值为文档，对其子文档创建索引，则加快通过子文档进行查找的速度
3. 唯一索引： 创建时希望索引的域有不同的值，也可以通过这个方法来限制域的值
	`db.class3.ensureIndex({name:1},{'unique':true})`
4. 覆盖索引：查找时，只获得索引项的内容，而不是去连接其他文档内容，这样从索引表就可以得到查询结果，提高查询效率
5. 稀疏索引（间隙索引）：只针对有指定域的文档创建索引表，没有该域的文档不插入到索引表中
	`db.class3.ensureIndex({age:1},{sparse:true})`
6. 文本索引：使用文本索引可以快速进行文本检索，在较长的字符串搜索中比较有用
	`db.class2.ensureIndex({msg:'text',description:'text'})`	创建索引
	`db.class2.find({$text:{$search:"old"}},{_id:0})`				通过单词索引，如果有其中任意一个单词就会被搜索
	`db.class2.find({$text:{$search:"\"city is\""}},{_id:0})`	搜索包含空格的语句，要用转义字符
	`db.class2.find({$text:{$search:"city -big"}},{_id:0})`		搜索某个，不包含某个
	`db.class2.getIndexes()`<br>`db.class2.dropIndex(name)`		删除文本索引

*1 表示为该域创建正向索引，-1表示逆向索引*
*系统自动为_id创建索引*
*_id索引不能被删除*

索引约束
1. 影响插入 删除 修改数据的效率。当发生数据修改时，索引必须同步更新
2.	索引也占用一定的空间，所以当数据量比较小时不是以创建索引


固定集合：
mongodb中可以创建固定大小的集合，称之为固定集合，固定集合性能出色且适用于很多场景
比如：日志处理，临时缓存
特点：	插入输入快
		顺序查询速度快
		能够淘汰早期数据

创建固定集合
`db.createColltion(colltion_name,{capped:true,size:10000,max:1000})`
`db.createCollection("log",{capped:true,size:1000,max:3})`

size	:	表示设置的固定集合的大小	单位 kb
max		:	表示固定集合中存放多少条文档

聚合
对数据文档进行整理统计

db.collect_name.aggregate()
功能：	聚合函数，配合聚合条件进行数据整理

聚合操作符

$group		分组，由具体的分组操作符来定


$sum		`db.class3.aggregate({$group:{_id:'$gender',num:{$sum:1}}})`
$avg		`db.class3.aggregate({$group:{_id:'$gender',num:{$avg:'$age'}}})`
$min		`db.class3.aggregate({$group:{_id:'$gender',num:{$min:'$age'}}})`
$max		`db.class3.aggregate({$group:{_id:'$gender',num:{$max:'$age'}}})`
$first		`db.class3.aggregate({$group:{_id:'$gender',num:{$first:'$age'}}})`
$last		`db.class3.aggregate({$group:{_id:'$gender',num:{$last:'$age'}}})`


$project	用于修饰文档的显示结构
值同find第二个字段相同,可以改变显示的域名
`db.class3.aggregate({$project:{_id:0,Name:'$name',Age:"$age"}})`

$match 过滤数据
值和qurey 一样 
db.class3.aggregate({$match:{age:22}})

$limit		显示前几条数据
db.class3.aggregate({$limit:2})

$skip		跳过几条数据
db.class3.aggregate({$skip:2})

$sort		排序
值同sort一样
db.class3.aggregate({$sort:{age:1}})

聚合管道
前一个聚合操作的结果给后一个聚合操作执行

格式：	将多个聚合操作放到一个[ ]中
`db.class3.aggregate([{$match:{gender:'m'}},{$sort:{age:1}},{$project:{_id:0}}])`



###**GridFS	大文件存储**

文件的数据库存储
1. 在数据库中以字符串的方式存储文件在本地的路径
2. 将文件以二进制数据方式存储在数据库中

GridFS:	时mongodb中存储大文件的一种方案。mongodb中认为超过16M的文件为大文件

将文件存储在mongodb数据库中，通过两个集合共同完成该文件的存储

fs.files:		存储文件的相关信息 比如 文件名 filename 文件类型content_type 等
fs.chunks:	实际存储文件内容，以二进制方式分块存储。将大文件分成多个小块，每小块占一条文档

mongofiles -d dbname put filename

1. 查看文件信息
db.fs.files.find().pretty()
2. 查看具体文件内容
db.fs.chunks.find({files_id:ObjectId("5ba9f4f44d5a5d294c063a51")})
*files_id:为fs.files集合中文档中的_id值*

优点：存储方便，没有文件个数限制	方便移植
缺点：读写效率低，只能整体修改，不能分块更新


###游标

1. 防止网络拥塞，造成数据传输慢
2. 避免用户解析带来的体验差，可以进行后段解析

使用方法
var cursor = db.class3.find()
cursor.hasNext()
cursor.next()


##**通过Python操作mongodb数据库**
数据库接口：	pymongo

```python
		from pymongo import MongoClient
		import pymongo
		#创建mongo的连接对象
		coon = mongoClient('localhost',27017)
		#选择要连接的数据库
		db = conn.stua  #   __getitem__     __setitem__
		#db = conn['stu']
		#选择要连接的集合
		my_set = db.class3
		#my_set = db['class3']
```

print(my_set)
print(dir(my_set))



增	insert()	insert\_many()	insert_one()	save()
删
remove()
功能：	删除一个文档
参数：	可以通过query条件删除
	可以通过文档的_id值进行删除

改	
update()


update_many
update_one


查	
find()
功能：查找数据库
参数：同mongoshell中find函数参数，需要符合python语法
返回值：可迭代的游标对象

游标对象的属性
next()
limit()
skip()
sort()
count()

find_one()	返回值为查找到一个文档的返回值

find({'age':{'$gt':20}})
find({'$or':[{'name':'zhang'},{'age':{'$gt':20}}]})

find_and_modify
find_one
find_one_and_delete
find_one_and_replace
find_one_and_update

####索引	
create_index()
ensure_index()


```python
#创建索引
index = my_set.ensure_index('name')
#创建复合索引
index = my_set.ensure_index([('name',1),('King',1)])

##先创建索引对象
index1 = IndexModel([('name',1),('King',-1)])
index2 = IndexNodel([('king_name',1)])
#通过create_indexes生成索引
indexes = my_set.create_indexes([index1,index2])
```

list_indexes() --------->>	getIndexes()

删除索引：
drop_index()
drop_indexes()


####聚合
aggregate()
功能：	实现mongo的聚合操作
参数：mongo shell 中聚合函数参数一致
返回值：迭代对象 同 find的返回值类型
	
####文件的存储

gridfs文件提取

普通文件以二进制方式存入数据库



























###
