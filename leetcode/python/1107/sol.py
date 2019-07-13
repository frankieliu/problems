In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1107.new-users-daily-count.database.json

Can anyone help me figure out why this code does not work?

https://leetcode.com/problems/new-users-daily-count/discuss/326971

* Lang:    python
* Author:  maoyic
* Votes:   0

select a.activity_date as login_date,count(distinct a.user_id) as user_count  
from Traffic a
where datediff("2019-06-30",a.activity_date)<=90 and a.activity="login" and a.user_id not in 
(select user_id from Traffic where activity="login" and datediff("2019-06-30",activity_date)>90) 
group by login_date

