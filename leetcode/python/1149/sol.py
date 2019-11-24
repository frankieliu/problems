In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1149.article-views-ii.database.json

MSSQL Self Join

https://leetcode.com/problems/article-views-ii/discuss/363022

* Lang:    python
* Author:  EmmaZelda
* Votes:   1

SELECT DISTINCT v1.viewer_id AS id
FROM views v1
JOIN views v2
ON v1.viewer_id = v2.viewer_id
AND v1.view_date = v2.view_date
AND v1.article_id != v2.article_id
ORDER BY 1;
