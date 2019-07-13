In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1045.customers-who-bought-all-products.database.json

MySQL subquery

https://leetcode.com/problems/customers-who-bought-all-products/discuss/294748

* Lang:    python
* Author:  ms25
* Votes:   11

```
select customer_id
from customer c
group by customer_id
having count(distinct product_key)=(select count(distinct product_key) from product)


```
