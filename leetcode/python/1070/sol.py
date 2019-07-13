In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1070.product-sales-analysis-iii.database.json

Is the expected solution correct?

https://leetcode.com/problems/product-sales-analysis-iii/discuss/304110

* Lang:    python
* Author:  hstangnatsh
* Votes:   3

Shortened the second test case for displayability. Below is the table screenshot. 
Expected output of OJ is actually the **minimum** year of a product_id, with quantity and price of the **first** row. That\'s obviously an outcome from query similar with 
```
select product_id, min(year), quantity, price 
from Sales 
group by product_id 
``` 
in which those ungrouped fields with mutiple values only shows the first row.
It hardly has anything to do with the discreption "product id, year, quantity, and price **for the first year** of every product sold."
![image](https://assets.leetcode.com/users/hstangnatsh/image_1559483193.png)
![image](https://assets.leetcode.com/users/hstangnatsh/image_1559483221.png)
My failed code was:
```
select Sales.product_id as product_id, Sales.year as first_year, quantity, price
from Sales, (select product_id as id, min(year) as my
from Sales
group by product_id) t
where Sales.product_id=t.id and Sales.year=t.my
order by product_id
```
