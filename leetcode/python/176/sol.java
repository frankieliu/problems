
Why does this not work ? ( by using limit )

https://leetcode.com/problems/second-highest-salary/discuss/53024

* Lang:    java
* Author:  number_2
* Votes:   0

    SELECT 
      IF(SUM< 1, NULL, s) AS salary 
    FROM
      (SELECT 
        salary AS s,
        COUNT(salary) AS SUM
      FROM
        Employee 
      ORDER BY salary DESC 
      LIMIT 1, 1) sub
