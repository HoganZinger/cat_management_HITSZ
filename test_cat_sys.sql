use my_cat_sys;
select * from userinfo;






















-- select * from userinfo;
-- select * from cat;
-- select * from feed;
-- select c.cat_name,DATE_FORMAT(a.aprnc_time,'%Y-%m-%d %H:%i:%s'),l.location_where from cat c,appearance a,location l
-- 	where c.cat_id=a.aprnc_cat_id 
--     and a.aprnc_location_id=l.location_id;

-- select * from appearance;
-- select * from location;

-- select c.cat_name,cf.foodtype_name,l.location_where,
-- 	DATE_FORMAT(f.feed_time,'%Y-%m-%d %H:%i:%s'),u.user_account
-- 	from feed f,catfood cf,cat c,userinfo u,location l
-- 	where c.cat_id=f.feed_cat_id
--     and f.feed_foodtype_id=cf.foodtype_id
--     and u.user_id=f.feed_user_id
--     and l.location_id=f.feed_loacation_id

-- select c.cat_name,c.cat_type,c.cat_gender,sr.sick_content,ph.hsptl_name,
-- 	u.user_account,sr.sick_cost
-- 	from userinfo u,cat c,sickness_record sr,pet_hospital ph
-- 	where sr.user_id=u.user_id and sr.cat_id=c.cat_id
--     and sr.hospital_id=ph.hsptl_id
-- delete from userinfo where user_id=14;
-- select * from userinfo;
-- select cat_name from cat
