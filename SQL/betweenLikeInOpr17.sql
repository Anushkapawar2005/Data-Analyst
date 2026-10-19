select * from employee2;

-- salary between 40000 and 60000
select first_name,last_name,salary from employee2 where salary between 40000 and 60000;

--email address end with gmail.com
select first_name,last_name,email from employee2 where email like '%@gmail.com';
select first_name,last_name,email from employee2 where first_name like '%a';     --start me a
select first_name,last_name,email from employee2 where first_name like 'j%';       --last me j

--emp belongs to either the 'finance' or 'marketing' department the IN operator
select first_name,last_name,department from employee2 where department in ('Finance','Marketing');