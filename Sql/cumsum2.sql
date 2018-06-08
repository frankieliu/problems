create table tablea (
    match_date            number,
    time            number,
    team            number,
    points_scored   number);

create table tableb (
    match_date        number,
    home_team   number,
    away_team   number);

insert into tablea values (20130818,1400,1,2);
insert into tablea values (20130818,1402,1,3);
insert into tablea values (20130818,1407,2,2);
insert into tablea values (20130818,1410,2,3);
insert into tablea values (20130818,1412,1,2);
insert into tablea values (20130822,1550,4,2);
insert into tablea values (20130822,1552,5,3);
insert into tablea values (20130822,1553,5,2);
insert into tablea values (20130822,1555,5,3);
insert into tablea values (20130822,1559,4,2);

insert into tableb values (20130818,2,1);
insert into tableb values (20130822,4,5);

create table cc as (select b.match_date, a.time,
(case when a.team = b.home_team then a.points_scored else 0 end) as home_points,
(case when a.team = b.away_team then a.points_scored else 0 end) as away_points,
sum(case when a.team = b.home_team then a.points_scored else 0 end) over (partition by a.match_date order by a.time) as cum_home_points,
sum(case when a.team = b.away_team then a.points_scored else 0 end) over (partition by a.match_date order by a.time) as cum_away_points
from TableB b join TableA a
on a.team in (b.home_team, b.away_team) and b.match_date = a.match_date);

