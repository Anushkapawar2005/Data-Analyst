create table users (
	 user_id int primary key,
	 name varchar(50) not null,
	 email varchar(100) unique,
	 age integer check (age>18),
	 reg_date timestamp  default current_timestamp
);

--inserting data into table  - comment
insert into users (user_id,name,email,age)
values (1,'anu pawar','ap2214.gemail.com',22);

insert into users (user_id,name,email,age)
values (2,'anu pawar','apawar2214.gemail.com',19);

select * from users;