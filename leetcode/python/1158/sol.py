In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1158.market-analysis-i.database.json

A simple MYSQL solution beats 100% so far

https://leetcode.com/problems/market-analysis-i/discuss/357761

* Lang:    python
* Author:  leoatcle
* Votes:   2

```
SELECT user_id AS buyer_id, join_date, COALESCE(COUNT(o.order_id),0) AS orders_in_2019
FROM Users u
LEFT JOIN Orders o ON u.user_id = o.buyer_id AND YEAR(order_date)=\'2019\'
GROUP BY user_id
ORDER BY user_id
```
