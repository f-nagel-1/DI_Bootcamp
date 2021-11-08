--select * 
--from students

--select first_name, last_name
--from students

select first_name, last_name

from students
--where student_id = 2
--where last_name = 'Benichou' or first_name = 'Marc'
--where last_name = 'Benichou' or first_name = 'Marc'
--where first_name ilike '%a%'
--where first_name ilike 'A%'
--where first_name ilike '%a'
--where first_name like '%a_'
--where student_id IN (1,3);
where birth_date > '2000-01-01';