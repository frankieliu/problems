In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1098.unpopular-books.database.json

MySQL - Filter first and Join later for better performance.

https://leetcode.com/problems/unpopular-books/discuss/324871

* Lang:    python
* Author:  rkonda
* Votes:   2

This solution is easy to visualize and readable. Filter first and join later will perform better if the data set is huge is required run in distributed environment.
```
select 
b.book_id,
b.name
from 
(select * from books where available_from <= "2019-05-23") b 
left join (select * from orders where dispatch_date >= "2018-06-23") o
on b.book_id=o.book_id 
group by b.book_id,b.name
having sum(o.quantity) is null or sum(quantity)<10
