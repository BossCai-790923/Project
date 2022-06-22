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


delete from students where name like 'B%';
-- delete from <TABLE NAME> where <filter condition>
select * from students;



delete from students where height < 1.7;
select * from students;


-- very dangerous
delete from students;
select * from students;