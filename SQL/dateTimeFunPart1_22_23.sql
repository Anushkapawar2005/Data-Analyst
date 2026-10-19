select * from products;

-- 1. now() - get current date and time

select now() as current_datetime;

--2. current_date() - get current date
select current_date as today_date;
select added_date , current_date ,(current_date - added_date) as days_difference from products;

--3. Extract() - extract part of a date   -- extract the year,month,and day from added_date column,
select product_name, 
       extract(year from added_date) as year_added, 
	   extract(month from added_date) as month_added, 
	   extract(day from added_date) as day_added from products;

--4. age() - calculate age between date
select product_name ,
       age(current_date,added_date) as age_since_added from products;

--5. to_char() - format dates as strings
--format added_date in a custom format (DD-MM-YYYY)
select product_name, to_char(added_date,'DD-MM-YYYY') as Formated_date from products;
select product_name, to_char(added_date,'DD-Mon-YY') as Formated_date from products;
select product_name, to_char(added_date,'DD-Month-YY') as Formated_date from products;

--6. date_part() - get specific date part
--extract the day of the work from added_date   --dow , month , week , day - you can search on chat gpt
select product_name,added_date,
       Date_part('dow',added_date) as day_of_work from products;           --day of week(dow)  - 0 to 6 eg 0 - sunday


--7. date_trunc() - truncate date to precision
--truncate added_date to the start of the month
select product_name, added_date,
       Date_Trunc('month',added_date) as month_start,
       Date_trunc('week',added_date) as week_start_day,
       Date_part('isodow',added_date) as day_of_week
from products; 

--8. interval - add or substract time intervals
-- add 6 months to the added_date
select product_name,added_date,
        added_Date + interval '6 days' as new_date from products;

--9. current_time() - get current time
--retrieve only the current time
select current_time as current_time;

--10. to_date() - convert string to date
--convert a string to a date format
select  to_date('28-11-2025', 'DD-MM-YYYY') as converted_date;

