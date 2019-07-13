In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1075.project-employees-i.database.json

MySQL

https://leetcode.com/problems/project-employees-i/discuss/308029

* Lang:    python
* Author:  Jc_Qu
* Votes:   1

```
# Write your MySQL query statement below
SELECT p.project_id
    , ROUND(AVG(e.experience_years),2) AS average_years
FROM Project AS p
    , Employee AS E 
WHERE p.employee_id = e.employee_id
GROUP BY 1 
```
