In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1132.reported-posts-ii.database.json

my mysql solution beats 100%

https://leetcode.com/problems/reported-posts-ii/discuss/342406

* Lang:    python
* Author:  annayu12
* Votes:   2

/* first, filter out distinct post labeled as spam
user_id | post_id | action_date | action | extra
2 | 2 | 2019-07-04 | report | spam
3 | 4 | 2019-07-04 | report | spam
4 | 3 | 2019-07-02 | report | spam

second, we will join removal table, add remove_date
user_id | post_id | action_date | action | extra | remove_date
2 | 2 | 2019-07-04 | report | spam | 2019-07-20 
3 | 4 | 2019-07-04 | report | spam | null
4 | 3 | 2019-07-02 | report | spam | 2019-07-18

third, calculate percentage of removal rate forr each date, assuming removal valid
action_date | removal_rate
2019-07-04 | 1.0
2019-07-02 | 0.5

fourth, calculate daily average removal precentage. Round to 2 decimal places 
*/
```
# Write your MySQL query statement below

select round(100 *sum(tmp.removal_rate)/count(*),2) as average_daily_percent 
from
(
	select a.action_date, 
	sum(case when r.remove_date is not null then 1 else 0 end)/count(*) as removal_rate
	from 
	( 
	  select distinct action_date, post_id from Actions 
	  where extra = "spam"
	 ) a
	left join Removals r
	on a.post_id = r.post_id
	group by a.action_date
)tmp

```
