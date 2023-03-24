--url=https://leetcode.com/problems/department-top-three-salaries/description/
select d.name Department, e.name Employee, e.salary Salary
from employee e
         join department d on e.departmentid = d.id
where (select count(distinct salary)
       from employee
       where salary > e.salary
         and departmentId = e.departmentId) < 3
