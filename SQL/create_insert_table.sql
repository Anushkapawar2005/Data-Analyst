create table Employee(
	employee_id serial primary key,
	name varchar(100) not null,
	position varchar(50),
	department varchar(50),
	hire_date date,
	salary numeric(10,2)
);

select * from employee;

Insert into employee(name,position,department,hire_date,salary)
      values ('anushka pawar','data analyst','data science','2025-05-15',65000.00),
       ('manasi khot','software engineering','data science','2025-06-17',55000.00),
      ('raj patil','data analyst','data science','2025-05-15',50000.00),
       ('ram jadhav','data analyst','data science','2025-05-15',70000.00);

ALter table employee
rename column position to position;

truncate table employee;
truncate table employee restart identity;

