-- --1
-- select first_name as "First Name", last_name as "Last Name"
-- from employees;

-- --

-- select distinct department_id
-- from employees
-- order by department_id;

-- --3

-- select *
-- from employees
-- order by first_name desc;

-- ---
-- select first_name, last_name, salary, trunc(0.15 * salary) as partial_salary
-- from employees;

-- ---5

-- select employee_id, first_name, last_name, salary
-- from employees
-- order by salary asc;

-- --
-- select sum(salary)
-- from employees;

-- --7
-- select max(salary), min(salary)
-- from employees;

-- --

-- select trunc(avg(salary))
-- from employees;


-- ---9

-- --select count(employee_id)
-- --from employees;



-- ---10

-- select upper(first_name)
-- from employees;


-- ---
-- select left(first_name, 3)
-- from employees;

-- --12

-- select concat(first_name, ' ', last_name)
-- from employees;

-- --

-- select first_name, last_name, length(concat(first_name, last_name))
-- from employees;


-- --14


-- select first_name
-- from employees
-- where first_name ilike '%1%' or first_name ilike '%2%' or first_name ilike '%3%' or first_name ilike '%4%' or first_name ilike '%5%' or first_name ilike '%6%' or first_name ilike '%7%' or first_name ilike '%8%' or first_name ilike '%9%' or first_name ilike '%0%';



-- 15

-- select *
-- from employees
-- limit 10;


-- ----part 2


-- --1
-- select first_name, last_name, salary
-- from employees
-- where salary between 10000 and 15000

-- --2
-- --select first_name, last_name, hire_date
-- --from employees
-- --where hire_date between '1987-01-01' and '1987-12-31';

-- --3
-- select first_name, last_name
-- from employees
-- where first_name ilike '%c%' and first_name ilike '%e%' ;

-- --4
-- select last_name, job_title, salary
-- from jobs
-- inner join employees
-- on employees.job_id = jobs.job_id
-- where job_title != 'Programmer' and job_title != 'Shipping Clerk' and salary != 4500 and salary != 10000 and salary != 15000 ;


-- --5
-- select last_name
-- from employees
-- where length(last_name) = 6;

-- --6
-- select last_name
-- from employees
-- where last_name ilike '__e%';

-- ---7

-- select distinct job_title
-- from employees
-- inner join jobs
-- on employees.job_id = jobs.job_id

-- --8

-- select *
-- from employees
-- where upper(last_name) in ('Jones', 'Blake', 'Scott', 'King', 'Ford')