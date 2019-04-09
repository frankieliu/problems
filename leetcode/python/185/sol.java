
This one is Faster than before\u2026\u2026

https://leetcode.com/problems/department-top-three-salaries/discuss/53743

* Lang:    java
* Author:  localhost7
* Votes:   0

    SELECT d.name As Department,
           e.name AS Employee,
           e.Salary As Salary
    FROM
    
    #top 3 Salary
      ( SELECT d_id,salary, @num := if(@type = d_id, @num + 1, 1) AS row_number, @type:= d_id AS dummy
       FROM
         (SELECT @num := 0, @type := '') r,
         ( SELECT DepartmentId  AS d_id,
                  salary
          FROM Employee
          GROUP BY salary,
                   DepartmentId 
          ORDER BY DepartmentId ,
                   salary DESC )AS xy
       GROUP BY d_id,
                salary
       HAVING row_number <=3
       ORDER BY d_id,
                salary DESC )AS xyz
    
     INNER JOIN Employee e ON e.salary = xyz.salary and e.DepartmentId =d_id
     INNER JOIN Department d ON  d.id=xyz.d_id
