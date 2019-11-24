In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1179.reformat-department-table.database.json

MySQL/PostgreSQL solutions

https://leetcode.com/problems/reformat-department-table/discuss/376357

* Lang:    python
* Author:  quabouquet
* Votes:   4

```
select id, 
	sum(case when month = \'jan\' then revenue else null end) as Jan_Revenue,
	sum(case when month = \'feb\' then revenue else null end) as Feb_Revenue,
	sum(case when month = \'mar\' then revenue else null end) as Mar_Revenue,
	sum(case when month = \'apr\' then revenue else null end) as Apr_Revenue,
	sum(case when month = \'may\' then revenue else null end) as May_Revenue,
	sum(case when month = \'jun\' then revenue else null end) as Jun_Revenue,
	sum(case when month = \'jul\' then revenue else null end) as Jul_Revenue,
	sum(case when month = \'aug\' then revenue else null end) as Aug_Revenue,
	sum(case when month = \'sep\' then revenue else null end) as Sep_Revenue,
	sum(case when month = \'oct\' then revenue else null end) as Oct_Revenue,
	sum(case when month = \'nov\' then revenue else null end) as Nov_Revenue,
	sum(case when month = \'dec\' then revenue else null end) as Dec_Revenue
from department
group by id
order by id
```
