--url=https://leetcode.com/problems/department-highest-salary/description/
with emsalary as
         (select max(salary) max_salary, departmentid
          from employee
                   join department d on employee.departmentid = d.id
          group by departmentid)

select d.name as Department, e.name as Employee, e.salary as Salary
from employee e
join department d on e.departmentid = d.id
join emsalary em on e.departmentid = em.departmentid
where e.salary >= em.max_salary;