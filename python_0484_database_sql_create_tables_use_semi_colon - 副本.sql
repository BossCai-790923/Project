-- use semi colon after each line when you run the whole as a script

drop table if exists students;

create table students (
	id integer,
	name text,
	height real
);

insert into students (id, name, height) values (1, "Alice", 1.62);
insert into students values (2, "Bob", 1.73);
insert into students values (2, 'Tom', 1.80);


select * from students;
select * from students where height > 1.78;