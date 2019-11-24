In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1159.market-analysis-ii.database.json

MYSQL EASY  UNDERSTAND

https://leetcode.com/problems/market-analysis-ii/discuss/358311

* Lang:    python
* Author:  hashnopolis
* Votes:   2

SELECT user_id AS seller_id, IF(favorite_brand = item_brand, \'yes\', \'no\') AS 2nd_item_fav_brand
FROM Users LEFT JOIN
    (SELECT o1.seller_id, o1.item_id, o1.order_date
    FROM Orders o1 JOIN Orders o2
    ON o1.seller_id = o2.seller_id AND o1.order_date > o2.order_date
    GROUP BY o1.seller_id, o1.order_date
    HAVING COUNT(*) = 1) tmp
ON Users.user_id = tmp.seller_id
LEFT JOIN Items 
ON tmp.item_id = Items.item_id
ORDER BY user_id
