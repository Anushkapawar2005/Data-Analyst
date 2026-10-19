select * from products;

/* 1. 
CASE Function – Categorizing Based on Conditions
 We will categorize products into price ranges:

Expensive if the price is greater than or equal to 50,000.
Moderate if the price is between 10,000 and 49,999.
Affordable if the price is less than 10,000.
*/

select product_name,price,
       case 
	        when price>=50000 then 'Expensive'
			when price>=10000 and price<=49999 then 'Moderate'
			else 'Affortable'
	    End as price_category
from products;
