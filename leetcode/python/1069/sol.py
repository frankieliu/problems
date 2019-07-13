In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1069.product-sales-analysis-ii.database.json

Simple 1337ms solution

https://leetcode.com/problems/product-sales-analysis-ii/discuss/304304

* Lang:    python
* Author:  brandacus
* Votes:   4

```
SELECT product_id, SUM(quantity) AS total_quantity
FROM Sales
GROUP BY product_id
```
