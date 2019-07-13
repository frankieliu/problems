In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1083.sales-analysis-ii.database.json

Simple MySQL solution

https://leetcode.com/problems/sales-analysis-ii/discuss/311386

* Lang:    python
* Author:  tschijnmo
* Votes:   11

```
SELECT s.buyer_id
FROM Sales AS s INNER JOIN Product AS p
ON s.product_id = p.product_id
GROUP BY s.buyer_id
HAVING SUM(CASE WHEN p.product_name = \'S8\' THEN 1 ELSE 0 END) > 0
AND SUM(CASE WHEN p.product_name = \'iPhone\' THEN 1 ELSE 0 END) = 0;
```
