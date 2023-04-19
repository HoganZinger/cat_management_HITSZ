use my_cat_sys;

truncate table appearance;
truncate table cat;
truncate table catfood;
truncate table feed;
truncate table location;
truncate table pet_hospital;
truncate table sickness_record;
truncate table userinfo;

insert into cat values
("小橘","麒麟尾橘猫","橘色",0,2,0),
("猫哥","英国短尾","白色",0,3,0),
("花花","橘猫","黄色",0,1,2),
("小花","英国短尾","黑白",1,4,0),
("白白","布偶","白色",1,5,0),
("包子","暹罗","淡紫色",1,6,0);
insert into catfood values
("火腿肠",1),
("饼干",2),
("猫条",3),
("鸡肉",4),
("冻干",5),
("罐头",6),
("罐装猫粮",7);
insert into userinfo values
("在干嘛呢","123456",1),
("小橘今天想我了吗","123456",2),
("数据库实验四好难写","123456",3),
("数据库实验五会不会更难呢","123456",4),
("地瓜多少钱","666666",5),
("秋风生渭水","123456",6),
("用户114514","114514",7),
("起床困难","654321",8),
("高速退学","123456",9),
("我爱学习","123456",10),
("亲亲猪猪","123456",11),
("不会学习","123456",12);
insert into location values
("学校操场",1),
("七栋楼下",2),
("八栋楼下",3),
("九栋楼下",4),
("十栋楼下",5),
("主楼附近",6),
("A栋附近",7),
("草坪",8);
insert into pet_hospital values
(1,"平山村宠物社康","西丽街道XX路10号"),
(2,"西丽宠物医院","桃源街道XX路20号"),
(3,"大学城宠物医院","塘朗街道XX路30号");
insert into appearance values
 #猫id，地点id，时间，key
(1,8,NOW(),1),
(1,4,DATE_SUB(NOW(),INTERVAL 75 MINUTE) ,2),
(1,2,DATE_SUB(NOW(),INTERVAL 150 MINUTE) ,3),
(1,1,DATE_SUB(NOW(),INTERVAL 225 MINUTE) ,4),
(1,6,DATE_SUB(NOW(),INTERVAL 300 MINUTE) ,5),
(2,5,NOW(),6),
(2,8,DATE_SUB(NOW(),INTERVAL 20 MINUTE) ,7),
(2,7,DATE_SUB(NOW(),INTERVAL 40 MINUTE) ,8),
(2,4,DATE_SUB(NOW(),INTERVAL 60 MINUTE) ,9),
(2,3,DATE_SUB(NOW(),INTERVAL 80 MINUTE) ,10),
(3,2,DATE_SUB(NOW(),INTERVAL 16 MINUTE) ,11),
(3,6,DATE_SUB(NOW(),INTERVAL 32 MINUTE) ,12),
(3,7,DATE_SUB(NOW(),INTERVAL 48 MINUTE) ,13),
(3,4,DATE_SUB(NOW(),INTERVAL 64 MINUTE) ,14),
(3,1,DATE_SUB(NOW(),INTERVAL 128 MINUTE) ,15),
(4,2,DATE_SUB(NOW(),INTERVAL 25 MINUTE) ,16),
(4,3,DATE_SUB(NOW(),INTERVAL 50 MINUTE) ,17),
(4,3,DATE_SUB(NOW(),INTERVAL 75 MINUTE) ,18),
(4,1,DATE_SUB(NOW(),INTERVAL 100 MINUTE) ,19),
(4,7,DATE_SUB(NOW(),INTERVAL 125 MINUTE) ,20),
(5,5,NOW(),21),
(5,8,DATE_SUB(NOW(),INTERVAL 11 MINUTE) ,22),
(5,6,DATE_SUB(NOW(),INTERVAL 22 MINUTE) ,23),
(5,3,DATE_SUB(NOW(),INTERVAL 33 MINUTE) ,24),
(5,2,DATE_SUB(NOW(),INTERVAL 44 MINUTE) ,25),
(6,4,NOW(),26),
(6,5,DATE_SUB(NOW(),INTERVAL 7 MINUTE) ,27),
(6,1,DATE_SUB(NOW(),INTERVAL 14 MINUTE) ,28),
(6,3,DATE_SUB(NOW(),INTERVAL 21 MINUTE) ,29),
(6,6,DATE_SUB(NOW(),INTERVAL 35 MINUTE) ,30);
insert into sickness_record values
#序号，用户id，猫id，医院id，花费，病症
(1,9,3,2,125.3,"肠胃炎"),
(2,5,3,2,70,"猫藓"),
(3,9,2,2,28.3,"寄生虫"),
(4,3,4,2,36,"瘟热"),
(5,2,3,1,57,"猫藓"),
(6,4,6,3,104,"肠胃炎");
insert into feed values
#人，猫，时间，地点，foodtype，序号
(12,	6,DATE_SUB(NOW(),INTERVAL 5 day)		,8,4,1),
(5,		5,DATE_SUB(NOW(),INTERVAL 2 day)		,3,3,2),
(8,		4,DATE_SUB(NOW(),INTERVAL 1 day)		,6,1,3),
(3,		3,DATE_SUB(NOW(),INTERVAL 2 day)		,7,2,4),
(6,		2,DATE_SUB(NOW(),INTERVAL 3 day)		,5,4,5),
(8,		1,DATE_SUB(NOW(),INTERVAL 5 minute)		,1,5,6),
(9,		5,DATE_SUB(NOW(),INTERVAL 30 minute)	,2,3,7),
(2,		3,DATE_SUB(NOW(),INTERVAL 150 minute)	,4,1,8),
(3,		2,DATE_SUB(NOW(),INTERVAL 33 minute)	,7,1,9),
(5,		4,DATE_SUB(NOW(),INTERVAL 77 minute)	,3,2,10),
(7,		6,DATE_SUB(NOW(),INTERVAL 16 minute)	,2,3,11),
(3,		4,DATE_SUB(NOW(),INTERVAL 26 minute)	,3,2,12),
(8,		4,DATE_SUB(NOW(),INTERVAL 36 minute)	,6,1,13),
(9,		3,DATE_SUB(NOW(),INTERVAL 46 minute)	,1,2,14),
(10,	2,DATE_SUB(NOW(),INTERVAL 66 minute)	,7,5,15),
(4,		1,DATE_SUB(NOW(),INTERVAL 76 minute)	,3,4,16),
(1,		5,DATE_SUB(NOW(),INTERVAL 86 minute)	,4,3,17),
(3,		2,DATE_SUB(NOW(),INTERVAL 666 minute)	,6,1,18),
(2,		5,DATE_SUB(NOW(),INTERVAL 3 hour)		,6,1,19),
(3,		4,DATE_SUB(NOW(),INTERVAL 1 hour)		,1,3,20),
(11,	6,DATE_SUB(NOW(),INTERVAL 12 hour)		,2,4,21),
(5,		5,DATE_SUB(NOW(),INTERVAL 6 hour)		,6,3,22),
(6,		4,DATE_SUB(NOW(),INTERVAL 2 hour)		,5,2,23),
(9,		2,DATE_SUB(NOW(),INTERVAL 7 hour)		,8,3,24),
(6,		2,DATE_SUB(NOW(),INTERVAL 8 hour)		,5,4,25),
(11,	1,DATE_SUB(NOW(),INTERVAL 57 minute)	,1,2,26),
(9,		5,DATE_SUB(NOW(),INTERVAL 305 minute)	,8,3,27),
(4,		3,DATE_SUB(NOW(),INTERVAL 73 hour)		,4,1,28),
(5,		2,DATE_SUB(NOW(),INTERVAL 222 minute)	,4,5,29),
(5,		4,DATE_SUB(NOW(),INTERVAL 57 hour)		,5,2,30);

-- SET SQL_MODE=@OLD_SQL_MODE;
-- SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
-- SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
-- SET autocommit=@old_autocommitcat;
