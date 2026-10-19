select * from products;

--get all the categories in uppercase
select upper(category) as category_capital from products;

--get all the categories in lowercase
select lower(category) as category_lower from products;

--joint product_name and category text with hypen use concat
select concat(product_name,'-',category) as product_details from products;

--Extract the five charcters from product_name
select substring(product_name,1,5) as short_name from products;

--count length
select product_name ,length(product_name) as count_of_char from products;

--remove leading and trailing spaces from string
select trim('  Monitor  ') as trimed_text;
select length (trim('  Monitor  ')) as trimed_text;

--replace word (column_name, old_name, new_name)
select replace(product_name,'phone','device') as updated from products;

--get the first 3 char 
select left(category,3) as category_char from products;
select right(category,3) as category_char from products;


