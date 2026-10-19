drop table if exists employee2;

create table employee2 (
   emp_id int primary key,
   first_name varchar(20) not null,
   last_name varchar(20) not null,
   email varchar(50) not null,
   department varchar(20),
   salary numeric(10,2),
   joining_date date,
   age int
);
select * from employee2;

--data import
copy employee2 (emp_id,first_name,last_name,email,department,salary,joining_date,age
) from 'E:\SQL\practice file\employee_data.csv' 
delimiter ',' 
csv header;