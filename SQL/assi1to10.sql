drop  table  if exists employee;
create table employee (
 emp_id serial primary key,
 first_name varchar(50) not null,
 last_name varchar(50) not null,
 department varchar(50),
 salary decimal(10,2)check(salary>0),
 joining_date date not null,
 age int check(age>=18)
);

insert into employee(first_name,last_name,department,salary,joining_date,age) values 
('Amit','Sharma','IT',60000.00,'2022-05-01',29),
('Neha','patel','HR',55000.00,'2021-08-15',32),
('Ravi','Kumar','Finance',70000.00,'2020-03-10',35),
('Anjali','Verma','IT',65000.00,'2019-11-22',28),
('Suresh','Reddy','Operations',50000.00,'2023-01-10',26);


select * from employee;

--retrieve first_name and department
select first_name,department from employee;

--update the salary of all employee int the IT department by incrasing the 10%
update employee set salary=salary+(salary*0.1) where department='IT';

--delete all employees who are older than 34
delete from employee where age>34;

--add a new column 'email' to the 'employee' table
alter table employee add column email varchar(100);

--rename department column to dep_name
alter table employee rename department to dep_name;

--retrieve the name of emp who joined aleter jan 1, 2021
select first_name,last_name,joining_date from employee where joining_date > '2021-01-01';

--change the data type salary column to data type
alter table employee alter column salary type integer using salary::integer;

--list all the emp age and salary dec
select first_name,age,salary from employee order by salary desc;

--inser new emp
insert into employee(first_name,last_name,dep_name,salary,joining_date,age)
values('raj','singh','marketing',60000,'2023-09-30',30);

--update age employee +1
update employee set age=age+1;

