--select * 
--from items
--order by price asc;
--where price >= 80
--order by price desc

--select *
--from customers
--limit 3

--select last_name
--from customers
--order by last_name desc

--create table purchases(
--purch_id serial,
--cust_id integer,
--prod_id integer,
--primary key (purch_id),
--foreign key (cust_id) references customers (customer_id),
--foreign key (prod_id) references items (item_id)
--);

--insert into purchases (cust_id) VALUES (1);

--insert into purchases (cust_id, prod_id) 
--values
-- (1, 1),
-- (1, 2),
-- (2, 1),
-- (2, 2),
-- (2, 3),
-- (1, 2),
-- (3, 2);


--select * 
--from purchases
--inner join customers
--on purchases.cust_id = customers.customer_id

--where purchases.cust_id = 4

--Purchases for a large desk AND a small desk 
-- no idea how

--insert into items (prod_name, price)
--values ('hard drive', 150)
--insert into purchases (cust_id, prod_id)
--values (1, 4)


--select first_name, last_name, prod_name
--from purchases
--inner join customers
--on purchases.cust_id = customers.customer_id
--inner join items
--on purchases.prod_id = items.item_id
--group by first_name, last_name, prod_name


----exercise 2 dvd rental

--select * 
--from customer

--select (first_name, last_name) as full_name
--from customer

--select distinct create_date
--from customer


--select *
--from customer
--order by first_name desc


--select film_id, title, description, release_year, rental_rate
--from film
--order by rental_rate asc

--select address, phone
--from address
--where district ilike 'Texas'


--select *
--from film
--where film_id in (15, 150)

---select film_id, title, description, length, rental_rate
--from film
--where title = 'Amelie'
--where title ilike ‘Am%‘;

--select *
--from film
--order by rental_rate
--limit 10

--offset 10 fetch first 10 row only;


--select first_name, last_name, amount, payment_date
--from customer
--inner join payment
--on customer.customer_id = payment.customer_id
--order by customer.customer_id

NO 13 DOES NOT WORK ? :

--select title 
--from film 
--inner join inventory 
--on film.film_id = inventory.film_id 
--where inventory.inventory_id IS NULL 
--order by title;

--select city, country
--from city
--inner join country
--on city.country_id = country.country_id