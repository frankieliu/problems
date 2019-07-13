In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1077.project-employees-iii.database.json

MySQL solution

https://leetcode.com/problems/project-employees-iii/discuss/311898

* Lang:    python
* Author:  mbodke41
* Votes:   1

```
select p.project_id, e.employee_id 
from project as p 
inner join employee as e 
on p.employee_id = e.employee_id 
where (p.project_id, e.experience_years) in (
                                                select p.project_id, max(e.experience_years)
                                                from project as p 
                                                inner join employee as e
                                                on p.employee_id = e.employee_id 
                                                group by p.project_id
                                             ) 
```
