-- 1 --
create table customers(
c_id int primary key auto_increment,
c_name varchar(20),
c_age tinyint unsigned,
c_sex enum("M","F"),
c_city varchar(20),
c_salary decimal(12,2));

-- 2 --
insert into customers values
(1,"zhangsan",20,"M","shanghai",3000),
(2,"lisi",23,"F","beijing",4000),
(3,"wangwu",22,"M","beijing",5000);

-- 3 --
create table orders(
o_id int,
o_name varchar(30),
o_price float(12,2),
foreign key(o_id)
references customers(c_id)
on delete cascade
on update cascade);

-- 4 --
insert into orders values
(1,"iphone",6000),
(2,"ipad",5000),
(3,"iwatch",4000),
(1,"mate9",4000),
(3,"r11",3500);

-- 5 --
select * from customers
where c_salary>4000 or c_age
limit 2;

-- 6 --
update customers set c_salary=c_salary*1.15 where c_age>25 or c_city in("shanghai","beijing");


-- 7 --
select * from customers 
where c_city="beijing" 
order by c_salary desc
limit 1;

-- 8 --
select * from customers
order by c_salary
limit 1;

-- 9 --
select customers.c_name,orders.o_name from customers 
inner join orders on c_id=o_id and customers.c_salary>5000;

-- 10 --
show create table orders;
alter table orders drop foreign key orders_ibfk_1;

-- 11 --
alter table customers modify c_id int;
alter table customers drop primary key;
