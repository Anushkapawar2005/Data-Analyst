create table Employee2(
	employee_id int primary key,
	name varchar(100) not null,
	position varchar(50),
	department varchar(50),
	hire_date date,
	salary numeric(10,2)
);

select * from employee2;

Insert into employee2(employee_id , name,position,department,hire_date,salary)
      values (101,'anushka pawar','data analyst','data science','2025-05-15',65000.00),
       (102,'manasi khot','software engineering','data science','2025-06-17',55000.00),
      (103,'raj patil','data analyst','data science','2025-05-15',50000.00),
       (104,'ram jadhav','data analyst','data science','2025-05-15',70000.00);


delete from employee2 where employee_id=103;

alter table employee2 drop column salary;

drop table if exists employee2;
