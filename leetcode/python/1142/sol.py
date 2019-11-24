In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1142.user-activity-for-the-past-30-days-ii.database.json

Mysql

https://leetcode.com/problems/user-activity-for-the-past-30-days-ii/discuss/348851

* Lang:    python
* Author:  huixingzhijia
* Votes:   0

```
select round(ifnull(count(distinct session_id)/count(distinct user_id),0),2) as average_sessions_per_user
from activity
where activity_date <= \'2019-07-27\' and activity_date > \'2019-06-27\'
```
