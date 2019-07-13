In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1068.product-sales-analysis-i.database.json

Simple SQL Solution with out any join keyword

https://leetcode.com/problems/product-sales-analysis-i/discuss/303688

* Lang:    python
* Author:  sakr17
* Votes:   2

```
# Write your MySQL query statement below

select Product.product_name, Sales.year, Sales.price
from Product, Sales
where Product.product_id = Sales.product_id


```
