/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2022/12/21 11:18:00                            */
/*==============================================================*/

create database my_cat_sys;
use my_cat_sys;

drop table if exists appearance;
drop table if exists cat;
#drop table cat_sickness;
drop table if exists catfood;
drop table if exists feed;
#drop table feed_cats;
drop table if exists location;
drop table if exists pet_hospital;
drop table if exists sickness_record;
drop table if exists userinfo;
drop view if exists what_cat_ate;

#drop trigger record_after_insert;

#drop table if exists What_Cat_Ate;

#drop index cat_type on Appearance;
#CREATE SCHEMA mycatsys;
/*==============================================================*/
/* Table: Appearance                                            */
/*==============================================================*/
create table Appearance
(
   aprnc_cat_id         int,
   aprnc_location_id    int,
   aprnc_time           time,
   aprnc_id             int not null,
   primary key (aprnc_id)
);

/*==============================================================*/
/* Index: cat_type                                              */
/*==============================================================*/
create index cat_type on Appearance
(
   aprnc_cat_id,
   aprnc_location_id
);

/*==============================================================*/
/* Table: Cat                                                   */
/*==============================================================*/
create table Cat
(
   cat_name             char(10),
   cat_type             char(10),
   cat_color            char(10),
   cat_gender           tinyint,
   cat_id               int not null,
   cat_counts_of_wtns   integer,
   primary key (cat_id)
);

/*==============================================================*/
/* Table: Cat_Sickness                                          */
/*==============================================================*/
-- create table Cat_Sickness
-- (
--    cat_id               int not null,
--    sick_id              int not null,
--    primary key (cat_id, sick_id)
-- );

/*==============================================================*/
/* Table: Catfood                                               */
/*==============================================================*/
create table Catfood
(
   foodtype_name        char(10),
   foodtype_id          int not null,
   primary key (foodtype_id)
);

/*==============================================================*/
/* Table: Feed                                                  */
/*==============================================================*/
create table Feed
(
   feed_user_id         int,
   feed_cat_id          int,
   feed_time            time,
   feed_loacation_id    int,
   feed_foodtype_id     int,
   feed_id              int not null,
   primary key (feed_id)
);

/*==============================================================*/
/* Table: Location                                              */
/*==============================================================*/
create table Location
(
   location_where       char(128),
   location_id          int not null,
   primary key (location_id)
);

/*==============================================================*/
/* Table: Pet_Hospital                                          */
/*==============================================================*/
create table Pet_Hospital
(
#   sick_id              int,
   hsptl_id             int not null,
   hsptl_name           char(20),
   hsptl_address        char(128),
   primary key (hsptl_id)
);

/*==============================================================*/
/* Table: Sickness_Record                                       */
/*==============================================================*/
create table Sickness_Record
(
   sick_id              int not null,
   user_id              int,
   cat_id               int,
   hospital_id          int,
   sick_cost            double,
   sick_content			char(128),
   primary key (sick_id)
);

/*==============================================================*/
/* Table: feed_cats                                             */
/*==============================================================*/
-- create table feed_cats
-- (
--    cat_id               int not null,
--    user_id              int not null,
--    primary key (cat_id, user_id)
-- );

/*==============================================================*/
/* Table: userinfo                                              */
/*==============================================================*/
create table userinfo
(
   user_account         char(15) not null,
   user_pwd             char(15) not null,
   user_id              int not null,
 #  feed_id              int,
   primary key (user_id)
);

/*==============================================================*/
/* View: What_Cat_Ate                                           */
/*==============================================================*/
delimiter $$
create VIEW  What_Cat_Ate
as

select f.feed_cat_id,c.cat_name,DATE_FORMAT(f.feed_time,'%Y-%m-%d %H:%i:%s'),cf.foodtype_name
	from feed f,catfood cf,cat c
	where f.feed_foodtype_id=cf.foodtype_id
		and c.cat_id=f.feed_cat_id
		
--  	group by f.feed_foodtype_id
    order by f.feed_cat_id asc

/*
select f.feed_cat_id,f.feed_foodtype_id,cf.foodtype_name 
	from feed f,catfood cf
	where f.feed_cat_id = any
		(select c1.cat_id from cat c1 order by c1.cat_id asc)
*/

;$$


-- alter table Cat_Sickness add constraint FK_Cat_Sickness foreign key (sick_id)
--       references Sickness_Record (sick_id) on delete restrict on update restrict;

-- alter table Feed add constraint FK_Feed_n_Location foreign key (location_id)
--       references Location (location_id) on delete restrict on update restrict;

-- alter table Feed add constraint FK_Foodtype_n_Feed foreign key (feed_foodtype_id)
--       references Catfood (foodtype_id) on delete restrict on update restrict;
/*
alter table Pet_Hospital add constraint FK_Sick_n_Hospital foreign key (sick_id)
      references Sickness_Record (sick_id) on delete restrict on update restrict;
*/
alter table Sickness_Record add constraint FK_Cat_n_Hospital foreign key (cat_id)
      references Cat (cat_id) on delete restrict on update restrict;

alter table Sickness_Record add constraint FK_User_n_Hospital foreign key (user_id)
      references userinfo (user_id) on delete restrict on update restrict;

-- alter table feed_cats add constraint FK_feed_cats foreign key (cat_id)
--       references userinfo (user_id) on delete restrict on update restrict;

-- alter table feed_cats add constraint FK_feed_cats2 foreign key (user_id)
--       references Cat (cat_id) on delete restrict on update restrict;

alter table userinfo add constraint FK_User_n_Feed foreign key (user_id)
      references Feed (feed_id) on delete restrict on update restrict;


create trigger record_after_insert 
after insert on cat
for each row
begin
-- 	if (old.cat_counts_of_wtns != 0)
/*
	update cat
    set cat_counts_of_wtns=old.cat_counts_of_wtns
		where cat_id=old.cat_id;
        */
end;
delimiter ;;
CREATE TRIGGER `record_after_aprnc` 
AFTER INSERT ON `appearance` FOR EACH ROW begin
	update cat
    set cat.cat_counts_of_wtns = cat.cat_counts_of_wtns+1
    where cat.cat_id = (select aprnc_cat_id from appearance
		order by aprnc_id desc limit 1) ;
end;;
