-- 4 sql types: 增删改查 -> INSERT / DELETE / UPDATE / SELECT


drop table if exists students;


create table students (
	id integer primary key,
	name text not null,
	height real not null
);


insert into students (id, name, height) values (1, "Alice", 1.62);
insert into students values (2, "Bob", 1.73);
insert into students values (3, 'Tom', 1.80);
insert into students (name, height) values ("Billy", 1.87);
insert into students (name, height) values ("lily", 1.66);


select * from students;


update students set name = 'Alice Li' where name = 'Alice';
select * from students;


update students set height = 1.74 where id = 2;
select * from students;


update students set name = "Lily Wang", height = 1.68 where id = 5;
select * from students;
