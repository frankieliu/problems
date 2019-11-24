In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1112.highest-grade-for-each-student.database.json

SQL Solution using row_number Faster than 100% users

https://leetcode.com/problems/highest-grade-for-each-student/discuss/330676

* Lang:    python
* Author:  swapna1487
* Votes:   4

```
SELECT t.student_id, t.course_id, t.grade
FROM 
	(SELECT student_id, course_id, grade, 
	row_number() over (partition by student_id order by grade desc, course_id asc) as r 
	FROM Enrollments) t
WHERE t.r=1
ORDER BY t.student_id asc
```
