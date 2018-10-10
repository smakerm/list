

##**基本SQL命令**

###1、SQL命令的使用规则
	1、每条命令必须以 ; 结尾
	2、SQL命令不区分字母大小写
	3、使用 \c 终止命令的执行
###2、库的管理
`为数据库账号修改密码:mysqladmin [-u用户名] [-p[旧密码]] password '新密码'`
####库的基本操作
|操作|命令|
---|---
查看已有的库|`show databases;`
创建库(指定字符集)|`create database 库名 default charset=utf8;`
查看创建库的语句|`show create database 库名;`
查看当前所在库|`select database();`
切换库|`use 库名;`
查看库中已有表|`show tables;`
删除库|`drop database 库名;`
数据库的授权|`grant 权限列表  on  数据库名.表名  to  用户名@客户机地址 identified   by   '密码';`

###表的管理
####1、表的基本操作
|操作|命令|
---|---
创建表|`create table 表名(字段名 数据类型,字段名 数据类型,...);`
查看创建表的语句(字符集)|`show create table 表名;`
查看表结构|`desc 表名;`
删除表|`drop table 表名;`
复制表|`create table 表名 select查询语句;`
复制表结构|`create table 表名 select * from 表名 where false;`
|||

####2、表字段的操作
`语法 ：alter table 表名 执行动作;`
|操作|命令|
---|---
添加字段(add)|1、添加到末尾：<br>`alter table 表名 add 字段名 数据类型;`<br>添加到开始：<br>`alter table 表名 add 字段名 数据类型 first;`<br>添加到指定位置：<br>`alter table 表名 add 字段名 数据类型 after 字段名`
删除字段(drop)|`alter table 表名 drop 字段名;`
修改数据类型(modify)|`alter table 表名 modify 字段名 新的数据类型;`
修改字段名(change)|`alter table 表名 change 旧名 新名 数据类型;`
修改表名(rename)|`alter table 表名 rename 新表名;`
|||


####3、表记录管理
|操作|命令|
---|---
在表中插入记录 | `insert into 表名 values(值1),(值2),....;`
查看表记录 | `select * from 表名;<br>select 字段名1,字段名2,... from 表名;`
更新表记录 | `update 表名 set 字段名=值,字段名=值,...where 条件;`<br>`注意：update语句后如果不加where子句,表中所有记录该字段的值都会更改`
删除表记录|`delete from 表名 where 条件;`<br>`注意：delete语句后如果不加where条件子句,将会把表中所有的记录全部删除`


###4、**SQL查询**
####1、总结(执行顺序)
		3、 select ... 聚合函数 from ...
		1、 where ...
		2、 group by ...
		4、 having ...
		5、 order by ...
		6、 limit ...;

####2、order by
1. 作用：对查询的结果进行排序
2. 语法格式：order by 字段名 排序方式;
3. 排序方式
	1. ASC(默认) ： 升序
	2. DESC   ：降序

####3、limit(永远放在SQL语句的最后写)
1. 作用：限制显示查询记录的条数
2. 用法
	1. limit n -->显示几条记录
	2. limit m,n
		m --> 从第几条记录开始显示,n表示显示几条
		## m的值是从0开始计数的,3从第四条记录开始
		limit 1,3 --> 显示 2、3、4 三条记录

####4、聚合函数
类型|作用
---|---
avg(字段名) | 求字段的平均值
sum(字段名) | 求字段的和
max(字段名) | 求字段的最大值
min(字段名) | 求字段的最小值
count(字段名)|统计该字段记录的个数

####5、group by
1. 作用 ：给查询的结果进行分组
2. 注意
	1. group by之后的字段必须要为select之后的字段
	2. 如果select之后的字段和group by之后的字段不一致,则必须要对select之后的该字段值做聚合处理
`select country,avg(gongji) from sanguo group by country;`

####6、having
1. 作用：对查询的结果进行进一步筛选
2. 注意
	1、having语句通常与group by语句联合使用,用来过滤由group by语句返回的记录集
	2、having语句的存在弥补了where关键字不能与聚合函数联合使用的不足,having操作的是聚合函数生成的显示列

####7、distinct
1. 作用：不显示字段的重复值
2. 注意
	1. distinct处理的是distinct和from之间的所有字段,所有字段值必须全部相同才能去重
	2. distinct不能对任何字段做聚合处理

####8、查询表记录时做数学运算
运算符 ：+ - * / %



####复杂查询方式
|查询类型|定义|语法格式|
|---|---|---|
|嵌套查询|把内层的查询结果作为外层查询的条件|`select查询语句 where 条件(select查询语句);`|
|多表查询||`select 字段名列表 from 表名列表; #笛卡尔积`<br>`select 字段名列表 from 表名列表where 条件;`|
|内连接查询|从表中删除与其他被连接表中没有匹配到的行|`select 字段名列表 from 表1 inner join 表2 on 条件;`|
|左连接查询|以左表为主显示查询结果|`slect 字段名列表 from 表1 left join 表2 on 条件;`|
|右连接查询|以右表为主显示查询结果|`slect 字段名列表 from 表1 right join 表2 on 条件;`|


###**5、索引(BTree)**
####1、索引的优缺点
1. 优点：加快数据的检索速度
2. 缺点：
	1. 索引需要动态维护,降低数据的维护速度
	2. 索引占用物理空间

####2、索引类型
#####1. 普通索引(MUL)
	1. 创建
			1. 创建表时创建: index(字段名),...
			2. 在已有表创建:`create index 索引名 on 表名;`
	2. 查看
		1. desc 表名;
		2. show index from 表名\G;
	3. 删除(只能一个一个删除)
		`drop index 索引名 on 表名;`
#####2. 唯一所以(UNI,字段值不允许重复,但可为NULL)
	1. 创建
		1. 创建表 `unique(字段名),...`
		2. 在已有表中创建 `create unique index 索引名 on 表名;`
	2. 删除
		drop index 索引名 on 表名;
#####3. 主键索引&自增长(PRI,不允许重复且不能为NULL)
	1. 注意
		一个表中只能有一个主键字段,常把编号设为主键字段
	2.创建表时创建主键
		1. 字段名 数据类型 primary key auto_increment,
		2. primary key(字段名)
	3. 在已有表中创建主键
		`alter table 表名 add primary key(字段名);`
	4. 删除主键
		1. 先删除自增长属性(modify)
		`alter table 表名 modify 字段名 数据类型;`
		2. 再删除主键(drop)
		`alter table 表名 drop primary key;`
	5. 在已有表中添加自增长属性(modify)
		`alter table 表名 modify 字段名 数据类型 primary key auto_increment;`
#####4. 外键索引(foreign key)
	1. 作用：让当前表字段值在另一个表的范围内选择
	2. 创建表时创建
	```		
		foreign key(参考字段名) 
		references 被参考表名(被参考字段名) 
		on delete 级联动作
		on update 级联动作
	```
	3. 在已有表中创建
	```
			alter table 表名 add foreign key(参考字段名) 
			references 被参考表名(被参考字段名)
			on delete 级联动作
			on update 级联动作
			## 在已有表中添加外键会受到表中原有数据的限制
	```
	4. 级联动作
		1. cascade(级联更新)
			1、当主表删除记录时,从表级联删除
			2、当主表更新被参考字段值时,从表级联更新
		2. restrict(检查外键限制,默认)
			1、当主表删除记录时,从表有相关联记录则不让主表删除
			2、当主表更新被参考字段值时,从表有相关联记录则不让主表更新
		3. set null
			1、当主表删除记录时,从表中相关联记录的参考字段值设置为NULL
			2、当主表更新记录时,从表中相关联记录的参考字段值设置为NULL
		4. no action(同restrict,立即检查外键限制)
	5. 使用规则
		1. 两张表被参考字段和参考字段数据类型要一致
		2. 被参考字段必须是key的一种,一般是primary key
	6. 删除外键
		1. 查看外键名
		`show create table 表名;`
		2. 删除外键限制
		`alter table 表名 drop foreign key 外键名;`




###**6、事务&事务回滚**
1. 事务定义
	一件事从开始发生到结束的整个过程
2. 属性
	1. 原子性：一个事务是不可分割的工作单位,事务中的各个操作要么都做,要么就都不做
	2. 一致性：事务必须从一个一致性状态到另一个一致性状态
	3. 隔离性：一个事务的执行不能被其他并发事务干扰
	4. 持久性：一个事务一旦提交,它对数据库的改变是永久性的
3. 事务及事务回滚的应用
	1. mysql中默认sql语句会自动commit到数据库
		`show variables like "autocommit";`
	2. 事务应用
		1. 开启事务
			`mysql> start transaction;`
			`## 此时autocommit被禁用,SQL命令不会对数据库中数据做修改`
		2. 终止事务
			`mysql> commit; | rollback;`
		3. 注意
			事务&事务回滚只针对对表记录的操作:增加、删除、修改,对创建库、创建表是无效的
	
###**7、Python数据库编程**
python数据库接口(Python DB-API)
1. Python提供的操作MySQL的模块
	模块名：pymysql
2. pymysql的使用流程
```	
	1、建立数据库连接
	2、创建游标对象
	3、使用游标对象的方法和SQL语句操控MySQL数据库
	4、提交commit
	5、关闭游标
	6、关闭数据库连接
	pymysql.connect --->>db ---> db.cursor() ----> 执行
```
3. 建立数据库连接
	1. 语法格式
	`对象名(db) = pymysql.connect("主机地址","用户名","密码","库名",charset="utf8")`
	2. connect对象(db)的方法
	|方法|作用|
	|---|---|
	|cursor()| 创建一个游标对象db.cursor()|
	|commit()|提交到数据库 db.commit()|
	|rollback()| 回滚 db.rollback()|
	|close()| 关闭与数据库的连接 db.close()|
	3、cursor游标对象(cur)的方法
	|execute() |执行sql命令|
	|fetchone() |取得结果集的第一条记录|
	|fetchmany(数字)| 取得结果集的 几条 记录|
	|fetchall()| 取得结果集的所有行|
	|close()| 关闭游标对象|
	|rowcount | 返回命令执行所影响的条数|

























###**数据导入导出**
####1、数据导入语法
```sql
load data infile "文件名"
into table 表名
fields terminated by "分隔符"
lines terminated by "分隔符"
## 文件名处要写绝对路径
```
####2、数据导入步骤
1. 在数据库中创建的对应的表
2. 查看数据库的搜索路径
`show variables like "secure_file_priv";`
3. 将文件拷贝到搜索路径中
`~$ sudo cp 文件名 搜索路径`
4. 执行导入命令
`mysql> load data infile ...`

####3、数据导出语法
```sql
select 字段名列表 from 表名
into outfile "文件名"
fields terminated by "分隔符"
lines terminated by "分隔符"
## 文件名必须要写绝对路径
```
####4、数据导出步骤
1. 查看数据库搜索路径
`show variables like "%secure%";`
2. 执行导出命令
`mysql> ...`

###**数据库备份与恢复**
####1、数据备份(在Linux终端操作)
1. 命令格式
`mysqldump -u用户名 -p 源库名 > 路径/XXX.sql`
2. 源库名的表示方式
--all-databases    备份所有库
库名               备份单个库
-B 库1 库2 ...     备份多个库
库名 表1 表2 ...   备份指定库的指定表
####2、数据恢复(在Linux终端操作)
1. 命令格式
`mysql -uroot -p 目标库名 < 路径/XXX.sql`
2. 从所有库的备份文件中恢复某一个库(--one-database)
`mysql -uroot -p --one-database 目标库名 < 路径/all_mysql.sql`
3. 注意
1. 恢复库时如果恢复到原有库会将表中数据覆盖,新增的表不会删除
2. 在恢复时如果要恢复的库不存在,则先要创建空库








###**运算符**
|类型|运算符|
---|---
数值比较运算符| =、!=、>、>=、<、<=
字符比较运算符| =、!=
逻辑比较| and、or
范围内比较| between and 、in 、not in
匹配空、非空|is null、is not null
模糊比较|like <br> _ : 匹配单个字符<br>% : 匹配0到多个字符



###**数据类型**
|数据类型|取值范围|用法|
|---|---|---|
|int 大整型(4个字节) | 取值范围：0~2**32 -1||
|tinyint 微小整型(1个字节) | 有符号(signed默认) -128~127<br>无符号(unsigned) 0~255||
|smallint 小整型(2个字节) | 取值范围：0~65535||
|bigint 极大整型(8个字节) | 取值范围：0~2**64 -1||
|float(4个字节,最多显示7个有效位)||字段名 float(m,n) m->总位数 n->小数位位数<br>float(5,2) 取值范围：-999.99~999.99
|double(8个字节,最多显示15个有效位)||字段名 double(m,n)
|decimal(M+2个字节,最多显示28个有效位)||decimal(M,D)
|char(定长)|宽度取值范围：1~255<br>不给定宽度默认宽度为1||
|varchar(变长)|宽度取值范围：1~65535||
|enum 单选|最多有65535个不同的值|`字段名 enum(值1,值2,...)`|
|set 多选|最多有64个不同的值|`字段名 set(值1,值2,...)`|
|year(年)| |YYYY|
|date(日期)| |YYYYMMDD|
|time(时间)|| HHMMSS|
|datetime(日期时间)|不给值默认返回NULL|YYYYMMDDHHMMSS|
|timestamp(日期时间) |不给值默认返回系统当前时间|YYYYMMDDHHMMSS|






















