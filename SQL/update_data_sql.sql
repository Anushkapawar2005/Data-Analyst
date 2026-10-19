drop table if exists user_table;
--create the user table
create table if not exists user_table(
	user_id serial primary key,
	username varchar(50) not null,
	email varchar(100) not null,
	age int,
	city varchar(50)
);

select * from user_table;

insert into user_table (username,email,age,city) values
('rajes','rajes@gmail.com',19,'sangli'),
('ram','ram@gmail.com',28,'miraj'),
('sita','sita@gmail.com',38,'miraj');

select user_id,username from user_table;

update user_table set age= 26 where username='rajes';


select * from user_table order by username asc;

update user_table set city='chenai' where age>30;

update user_table set city='chenai', age=20 where age=38;

update user_table set age=age+1 where email like '%@gmail.com';

--to rename the username column to full_name
alter table user_table rename column username to full_name;

--to change the age column data type from int to smallint
alter table user_table alter column age type smallint;  --smallint 2byte and int 4byte

--to add not null constraint to city column
alter table usser_table alter column city set not null;

--adding check constraint age column
alter table user_table add constraint age check(age>=18);

--remove constraint
alter table user_table f=drop constraint age;

--rename table name
alter table user_table rename to customers;

alter table customers rename to user_table;



