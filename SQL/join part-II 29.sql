

--full outer join  : both table records combile

select e.employee_id,e.first_name,e.last_name, d.department_id,d.department_name from employees3 e full outer join departments d 
on e.department_id=d.department_id;

--cross join  : one table with each department
select e.first_name,e.last_name,d.department_name from employees3 e cross join departments d;

--self join : only one table use - same department
select e1.first_name as emp_name1,
       e2.first_name as emp_name2
from employees3 e1 join employees3 e2
on e1.department_id=e2.department_id;

--condition include
select e1.first_name as emp_name1,
       e2.first_name as emp_name2
from employees3 e1 join employees3 e2
on e1.department_id=e2.department_id and e1.employee_id != e2.employee_id;

-- it show ddepartment name
select e1.first_name as emp_name1,
       e2.first_name as emp_name2,
	   d.department_name
from employees3 e1 join employees3 e2
on e1.department_id=e2.department_id and e1.employee_id != e2.employee_id
join
departments d
on 
e1.department_id=d.department_id;