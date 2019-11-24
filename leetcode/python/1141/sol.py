In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1141.user-activity-for-the-past-30-days-i.database.json

Simple MySQL Group By solution

https://leetcode.com/problems/user-activity-for-the-past-30-days-i/discuss/349492

* Lang:    python
* Author:  varunu28
* Votes:   0

```
# Write your MySQL query statement below
SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
GROUP BY activity_date
HAVING DATEDIFF("2019-07-27", activity_date) < 30;
```
