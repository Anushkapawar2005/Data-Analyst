drop table  hospitals;
CREATE TABLE hospitals (
   Hospital_id serial primary key,
    Hospital_name varchar(100),
	location varchar(50),
	department varchar(50),
	doctors_count int,
	patients_count int,
	admission_date date,
	discharge_date date,
	medical_expenses numeric(12,2)
);

copy hospitals(hospital_name,location,department,doctors_count,patients_count,admission_date,discharge_date,medical_expenses)
from 'E:\SQL\practice file\Hospital_Data.csv'
CSV header;

select * from hospitals;

--1
select sum(patients_count) as total_patients from hospitals;

--2
select hospital_name, avg(doctors_count) as avg_doctors from hospitals group by hospital_name;

--3
select department, sum(patients_count) as total_patients from hospitals group by department order by total_patients desc limit 3;

--4
select distinct hospital_name, max(medical_expenses) as max_expenses from hospitals group by hospital_name 
order by max_expenses desc limit 1;

--5
select hospital_name,avg(medical_expenses) as avg_daily_expenses from hospitals group by hospital_name;

--6
select hospital_name,department,(discharge_date - admission_date) as stay_duration 
from hospitals order by stay_duration desc limit 1;

--7
select location,sum(patients_count) as total_patients from hospitals group by location;

--8
select department, avg(discharge_date - admission_date) as avg_stay_days from hospitals group by department;

--9
select department ,sum(patients_count) as total_patients from hospitals 
group by department order by total_patients asc limit 1;

--10
select extract(month from admission_date) as month, sum(medical_expenses) as total_expenses from hospitals 
group by month order by month;

