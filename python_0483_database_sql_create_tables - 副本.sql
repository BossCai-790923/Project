-- drop table ================================

drop table if exists students




-- create table ===============================

create table students (
	id integer,
	name text,
	height real
)


-- 1st line create table <TABLE NAME> (
-- you can define as many columns as you like
-- each column takes oneline, in this format: <COLUMN NAME> <COLUMN TYPE>
-- You can only use integer / text / real


-- Press F5 to refresh


-- insert records / lines / data into students table ========

insert into students (id, name, height) values (1, "Alice", 1.62)
-- insert into <TABLE NAME> (<COLUMN LIST>) values (<VALUES>)


insert into students values (2, "Bob", 1.73) -- you can omit the column list if you set values for all columns

insert into students values (2, 'Tom', 1.80)


-- select ===================================================

select * from students

select * from students where height > 1.78