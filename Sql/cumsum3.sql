drop table t;
drop table t2;

create table t ( 
id int, 
dt date, 
amt int 
); 

insert into t values (1, date'2016-10-01', 100); 
insert into t values (2, date'2016-10-02', 50); 
insert into t values (3, date'2016-10-03', -10); 
insert into t values (4, date'2016-10-04', 20); 
commit; 

select t.*, sum(amt) over (order by id) tot from t;
create table t2 as (select id,amt,1 as const from t) order by id;
select t2.*, sum(const) over (order by id) tot from t2;

