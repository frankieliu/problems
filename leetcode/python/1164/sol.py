In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1164.product-price-at-a-given-date.database.json

Easy to understand solution, beat 99.5%, no need for window function, just a simple union

https://leetcode.com/problems/product-price-at-a-given-date/discuss/367140

* Lang:    python
* Author:  tianqi2019
* Votes:   6

select distinct product_id, 10 as `price`
from Products
group by product_id
having (min(change_date) > "2019-08-16")

union

select p2.product_id, new_price
from Products p2
where (p2.product_id, p2.change_date) in

(
    select product_id, max(change_date) as recent_date
    from Products
    where change_date <= "2019-08-16"
    group by product_id
)
