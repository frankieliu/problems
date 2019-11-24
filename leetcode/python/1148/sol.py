In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1148.article-views-i.database.json

MySQL Soultion

https://leetcode.com/problems/article-views-i/discuss/370948

* Lang:    python
* Author:  user3529L
* Votes:   0

select distinct viewer_id id 
from Views 
where author_id = viewer_id order by id;
