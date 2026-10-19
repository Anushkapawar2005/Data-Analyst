select * from employee2;

--find employees where the email column is NULL (if_applicable),
select first_name,last_name,email from employee2 where email IS NULL;

-- emp sorted by salary desc
select first_name,last_name,email from employee2 order by salary;

--retrieve the top 5 highes-paid employee
select first_name,last_name,email from employee2 limit 3; 

select first_name,last_name,email from employee2 order by salary ASC limit 3;

select first_name,last_name,salary from employee2 order by salary ASC limit 3;

--retrieve a list of unique department
select distinct department from employee2;
select count (distinct department) from employee2;

select count (distinct department) as dep_unique_count from employee2;
