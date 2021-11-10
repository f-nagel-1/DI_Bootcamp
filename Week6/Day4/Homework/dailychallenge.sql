--create table orders (
--order_id integer primary key,
--order_date date
--
--);

--insert into orders
--values ('1', '2021-01-01'),
--('2', '2020-05-10');

--create table items (
--item_id int primary key,
--item_name varchar(50),
--item_quantity int,
--item_unit_price int,
--order_id int,
--foreign key (order_id) references orders (order_id)

--);

--insert into items
--values (1, 'book', 2, 5, 1),
--(2, 'ball', 3, 10, 2),
--(3, 'glass', 1, 10, 1),
--(4, 'cup', 6, 7, 2);


--Create a function that returns the total price for a given order.

--create or replace function total_price(oi int)
--returns int as $pricecalculation$
--begin
--return (select sum(item_unit_price * item_quantity) from items where order_id = oi);
--end;
--$pricecalculation$ language plpgsql;

bonus:

--select * from total_price(1);

--create table users (
--user_id int primary key,
--first_name varchar(50),
--last_name varchar(50)

--);

--alter table orders
--add user_id int;
--add foreign key (user_id) references users (user_id);

--insert into users
--values (100, 'Tom', 'Smith'),
--(101, 'Anna', 'Clarke');

--update orders 
--set user_id = 101
--where order_id = 2;


--create or replace function total_price_user(ui int)
--returns int 
--as $pricecalculationuser$
--begin
--return (select sum(item_unit_price * item_quantity) 
		--from items 
		--inner join orders
		--on items.order_id = orders.order_id
		--where user_id = ui);
--end;
--$pricecalculationuser$ language plpgsql;

--select * from total_price_user(101);
