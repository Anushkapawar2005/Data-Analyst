drop table if exists employee3;

create table employee3 (
   emp_id int primary key,
   first_name varchar(20) not null,
   last_name varchar(20) not null,
   email varchar(50) not null,
   department varchar(20),
   salary numeric(10,2),
   joining_date date,
   age int
);
select * from employee3;
