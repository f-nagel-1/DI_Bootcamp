-- create table customer (
--     customer_id serial not null,
--     year_joined integer not null,
--     primary key (customer_id)
-- );

-- insert into customer (customer_id, year_joined)
-- values
--     ('1', '2009'),
--     ('2', '2004'),
--     ('3', '2001'),
--     ('4', '2021');


-- create table customerprofile (
--     customerprofile_id serial not null,
--     first_name varchar(50),
-- 	last_name varchar(50),
--     primary key (customerprofile_id),
-- 	foreign key (customerprofile_id) references customer (customer_id)
-- );

-- insert into customerprofile (first_name, last_name)
-- values
--     ('Susan', 'Smith'),
--     ('Jo', 'Antler'),
--     ('Mikey', 'Dougan'),
--     ('Martin', 'Crane');

--     ---- why can i not insert more values`????
--     insert into customerprofile (customerprofile_id, first_name, last_name)
-- values
--     (5, 'Bob', 'Derek'),
--     (6, 'Ted', 'Darkthrone');


-- select customer_id, year_joined, first_name, last_name
-- from customerprofile
-- inner join customer
-- on customer.customer_id = customerprofile.customerprofile_id;

-- select customer_id, year_joined, first_name, last_name
-- from customerprofile
-- left join customer
-- on customer.customer_id = customerprofile.customerprofile_id;


-----