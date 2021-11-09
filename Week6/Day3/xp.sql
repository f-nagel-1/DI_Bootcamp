-- select name
-- from language

-- select title, description, name
-- from film
-- inner join language
-- on film.language_id = language.language_id

-- select title, description, name
-- from film
-- full join language
-- on film.language_id = language.language_id

-- --3
-- create table new_film(
-- new_id serial,
-- new_name varchar (50),
-- primary key (new_id)
-- );


-- insert into new_film (new_name)
-- values ('Terminator 1'), ('Amelie'), ('Pi');


-- --5

-- create table customer_review (
-- 	review_id serial not null,
-- 	film_id integer not null,
-- 	language_id integer,
-- 	title varchar (100),
-- 	score integer not null,
-- 	check (score between 1 and 11),
-- 	review_text text,
-- 	last_update timestamp default current_timestamp,
-- 	primary key (review_id),
-- 	foreign key (film_id) references new_film (new_id) on delete cascade,
-- 	foreign key (language_id) references language (language_id)
-- );

-- insert into customer_review(film_id, language_id, title, score, review_text)
-- values 
-- (1, 3, 'Amazing film', 10, 'well-directed with fantastic actors'),
-- (2, 3, 'What garbage', 1, 'waste of time, do not watch this');

-- --5
-- --insert into new_film (new_id, new_name)
-- --values (4, 'Terminator 2');
-- update customer_review 
-- set film_id = 2
-- where review_id = 4;

-- --6
-- --delete from new_film
-- --where new_id = 2
-- --select * from new_film

-- -----------
-- --exercise 1


-- --update film
-- --set language_id = 3
-- --where film_id between 20 and 25;
-- --where film_id between 25 and 30

-- --2
-- --customer_address_id_fkey => address_id is foreign key.
-- --address id is first created in the address table


-- --3
-- -- I think is can be deleted without problem ??

-- --4
-- select title
-- from film
-- left join inventory
-- on film.film_id = inventory.film_id
-- where inventory.inventory_id is null


-- --5
-- select title, rental_rate
-- from film
-- left join inventory
-- on film.film_id = inventory.film_id
-- where inventory.inventory_id is null
-- order by rental_rate desc
-- limit 30

-- ---6
-- select title
-- from film
-- inner join film_actor
-- on film.film_id = film_actor.film_id
-- inner join actor
-- on actor.actor_id = film_actor.actor_id
-- where description ilike '%sumo%' and first_name='Penelope' and last_name='Monroe';

-- --
-- select title, length, rating
-- from film
-- where description ilike '%documentary%' and length < 60 and rating = 'R';

-- --- no idea if this is correct
-- select title, first_name, last_name, rental_rate, return_date
-- from rental
-- inner join customer
-- on rental.customer_id = customer.customer_id
-- inner join inventory
-- on inventory.inventory_id = rental.rental_id
-- inner join film
-- on film.film_id = inventory.film_id
-- where first_name = 'Matthew' and last_name = 'Mahan' and rental_rate > 4.00 and return_date > '2005-07-28'


-- ---

-- select title, description, first_name, last_name, rental_rate
-- from rental
-- inner join customer
-- on rental.customer_id = customer.customer_id
-- inner join inventory
-- on inventory.inventory_id = rental.rental_id
-- inner join film
-- on film.film_id = inventory.film_id
-- where first_name = 'Matthew' and last_name='Mahan' and (title ilike '%boat%' or description ilike '%boat%')