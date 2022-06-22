drop table if exists students;


-- you can specify primary key when you declare a column
-- primary key is like the key in python dict, it doesn't allow duplicate
-- each table can only contain 1 primary key column

create table students (
	id integer primary key,
	name text,
	height real
);



insert into students (id, name, height) values (1, "Alice", 1.62);
insert into students values (2, "Bob", 1.73);
insert into students values (3, 'Tom', 1.80);


-- another benefit is, you don't need to specify the primary key column value
insert into students (name, height) values ("Billy", 1.87);
insert into students (name, height) values ("lily", 1.66);





select * from students;
select * from students where height > 1.78;