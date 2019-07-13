In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1084.sales-analysis-iii.database.json

easy solution faster

https://leetcode.com/problems/sales-analysis-iii/discuss/311964

* Lang:    python
* Author:  joshualovelife666
* Votes:   5

select product_id, product_name 
from product 
where product_id not in
(select product_id
from sales
where sale_date not between \'2019-01-01\' and \'2019-03-31\');
