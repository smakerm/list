1. 创建一个数据库名字为grade
use grade
2. 数据库中创建集合 名字为class
3. 集合中插入若干文档 文档格式为

```javascript
db.class.insert(
[
{name:'xiaohong',age:10,sex:'f',hobby:['draw','song','dance']},
{name:'xiaoming',age:5,sex:'m',hobby:['football','song']},
{name:'xiangwang',age:3,sex:'m',hobby:['draw','dance']}
]
)

db.class.insert(
{name:'xiaoling',age:7,sex:'f',hobby:['dance','pb']}
)
```
*插入的同时创建集合和使数据库真实创建*

4. 查找练习
查看该班中所有学生信息
db.class.find({},{_id:0})
查看班级中年龄为5岁的学生信息
db.class.find({age:5},{_id:0})
查看年龄大于6岁的学生信息
db.class.find({age:{$gt:6}},{_id:0})
查看年龄在4--8岁之间的学生
db.class.find({age:{$gt:4,$lt:8}},{_id:0})

查看年龄时4岁并且为男生的学生
db.class.find({$and:[{age:4},{sex:'m'}]},{_id:0})
db.class.find({age:4,sex:'m'},{_id:0})
查看年龄小于4岁多者大于8岁的学生
db.class.find({$or:[{age:{$gt:8},age:{$lt:4}}]},{_id:0})

查看年龄时4岁或者6岁的学生
db.class.find({age:{$in:[3,5]}},{_id:0})

查看兴趣爱好有2项的学生
db.class.find({hobby:{$size:2}},{_id:0})
查看兴趣爱好有画画的学生
db.class.find({hobby:'draw'},{_id:0})
查看兴趣爱好即喜欢画画有喜欢跳舞的学生
db.class.find({hobby:['draw','dance']},{_id:0})
统计兴趣爱好有三项的学生人数
db.class.find({hobby:{$size:3}},{_id:0}).count()
查看本班年龄第二大的学生
db.class.find().sort({age:-1}).skip(1).limit(1)

将学生年龄按照升序 姓名按照降序排序
db.class.find({},{_id:0}).sort({age:1},{name:-1})
统计学生兴趣的范围
db.class.distinct('hobby')
删除所有年龄 小于4的男生
db.class.remove({age:{$lt:4}},{sex:'m'})

将班中名字为小红的同学年龄变为8岁 兴趣爱好变为跳舞画画
db.class.update({name:'xiaohong'},{$set:{age:8,hobby:["dance","draw"]}})
追加小明同学兴趣爱好 唱歌
db.class.update({name:'xiaoming'},{$push:{hobby:'song'}})
增加小王兴趣爱好 吹牛和打篮球
db.class.update({name:'xiaoming'},{$push:{hobby:{$each:['song','cuit']}}})

增加小李兴趣爱好 跑步和唱歌，但保证和以前的爱好不重复
db.class.update({name:'xiaohong'},{$addToSet:{hobby:{$each:['song','dance']}}})
给该班所有男同学年龄增加1
db.class.update({sex:"m"},{$inc:{age:1}})
删除小明的sex属性
db.class.update({name:'xiaoming'},{$unset:{sex:1}})
删除小明兴趣爱好中的第一项
db.class.update({name:'xiaoming'},{$pop:{hobby:-1}})
将小红兴趣中画画一项删除
db.class.update({name:'xiaohong'},{$pull:{hobby:"draw"}})


使用之前的练习数据库
为数据增加分数域
source:{'chinese':88,'english':78,'math':98}

1. 按照性别进行分组，统计每组人数
db.class.aggregate({$group:{_id:'$sex',num:{$sum:1}}})
2. 按照学生姓名分组，过滤出有重命的同学
db.class.affregate([$group:{_id:'$name',num:{$num:1}},{$math:{num:{$gt:1}}}])
3. 统计每名男生的语文分数
db.class.aggregate([{$macth:{sex:'m'}},{$project:{_id:0,name:1.'source.chinese':1}}])
4. 将女生按照英语分数降序排列
db.class.aggregate([{$match:{sex:'w'}},{$sort:{'source.english':-1}}])
