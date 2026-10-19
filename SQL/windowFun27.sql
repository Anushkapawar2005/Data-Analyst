select * from products;
-- assign unique row no. to each product within same category
select product_name, category,price, 
   		ROW_NUMBER() over(Partition by category order by price desc) as row_number
from products;

select product_name, category,price, 
   		dense_rank() over(Partition by category order by price desc) as row_number
from products;


select product_name, category,price, 
   		sum(price) over(Partition by category order by price desc) as running_total
from products;