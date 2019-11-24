In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1173.immediate-food-delivery-i.database.json

MYSQL + CASE WHEN + AVG + ROUND

https://leetcode.com/problems/immediate-food-delivery-i/discuss/370500

* Lang:    python
* Author:  XIONGCODE
* Votes:   2

SELECT ROUND(AVG(CASE WHEN order_date = customer_pref_delivery_date 
                  THEN 1 ELSE 0 END)*100, 2) AS immediate_percentage
FROM delivery

