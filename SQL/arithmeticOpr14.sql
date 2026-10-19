select * from employee2;

select first_name,salary, (salary*0.10) as bonus from employee2;

--calculating new salary
select first_name,last_name,salary,
(salary*12) as annual_salary,
(Salary*0.05) as increment_amount,
(salary*1.05) as new_salary,
(salary+salary*0.05) as new_salary2
from employee2;