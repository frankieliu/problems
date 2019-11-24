In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1113.reported-posts.database.json

MySQL Solution

https://leetcode.com/problems/reported-posts/discuss/330526

* Lang:    python
* Author:  ellie7947
* Votes:   2

SELECT extra AS report_reason, COUNT(DISTINCT post_id) AS report_count
FROM Actions
WHERE action = \'report\' AND action_date = \'2019-07-04\'
GROUP BY extra
