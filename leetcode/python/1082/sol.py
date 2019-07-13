In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1082.sales-analysis-i.database.json

MySQL Solution

https://leetcode.com/problems/sales-analysis-i/discuss/311519

* Lang:    python
* Author:  bewestphal
* Votes:   2

```
SELECT seller_id
FROM Sales
GROUP BY seller_id
HAVING SUM(PRICE) >= all (
    SELECT SUM(PRICE)
    FROM Sales
    GROUP BY seller_id
)
 ```
