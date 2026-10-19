select * from products;

/* 1. CASE Function – Categorizing Based on Conditions
 We will categorize products into price ranges:

Expensive if the price is greater than or equal to 50,000.
Moderate if the price is between 10,000 and 49,999.
Affordable if the price is less than 10,000.
*/

select product_name, quantity,
     case 
	 when quantity>=10 then 'In stock'
	-- when quantity>5 and quantity<9 then 'limited stock'
	 when quantity between 6 and 9 then 'limited stock'
	 else 'out of stock soon'
	end as stock_status
from products;

/* 2. CASE with AND & OR Operators – Stock Status
We will classify products based on quantity available:

In Stock if quantity is 10 or more.
Limited Stock if quantity is between 5 and 9.
Out of Stock Soon if quantity is less than 5.
*/
select product_name, category,
     case 
	 when category like 'Electronics%' then 'Electronic item'
	 when category like 'Furnitures%' then 'Furniture item'
	 else 'Accessory item'
	end as category_status
from products;

