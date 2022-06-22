
-- Q) Show me the total count of player table
select count(*) from player



-- Q1) Show me all players
select * from player
-- select * from <TABLE_NAME>
-- * means all columns



-- Q2) Show me all players' name & birthday
select player_name, birthday from player
-- select <COLUMN_NAME_SEPARATED_BY_COMMA> from <TABLE_NAME>




-- Q3) Show me all players' name & birthday, player_name column, please rename the column name to 'Full Name'
select player_name as 'Full Name', birthday as 'Birthday' from player
-- as 'ALIAS_NAME' allows you to rename some column name




-- Q4) Show me all players whose weight is greater or equals than 190 pound
select * from player where weight >= 190
-- where allows you to filter records




-- Q5) Show me all players who are both weight greater than 190 pound and height greater than 190 cm
select * from player where weight > 190 and height > 190
-- you can put multiple filter conditions, joined by 'and'



-- Q6) Show me player 'Aaron Doran' information
select * from player where player_name = 'Aaron Doran'




-- Q7) Show me all players whose first name is 'Aaron'
select * from player where player_name like 'Aaron %'
-- Use 'like' to do fuzzy search, wildcard search
-- % matches anything




-- Q8) Show me all players whose name 1st letter is T, 3rd letter is m
select * from player where player_name like 'T_m%'
-- Use 'like' to do fuzzy search, wildcard search
-- _ matches single character





-- Q9) Show me all players whose ids are in (1, 5, 10)
select * from player where id in (1, 5, 10)
-- Use 'in' to do set filter -> id must be in set (1,5,10)





-- Q10) Show me all players whose height is between 180 and 190
select * from player where height between 180 and 190
-- use between <SMALL> and <BIG> to do range search





-- Q11) Show me all matches whose goal is null
select * from match where goal is null
-- use 'is null' to restrict the column must has NO value

-- Q12) Show me all matches whose goal is not null
select goal from match where goal is not null
-- use 'is not null' to restrict the column must has value




-- Q13) show me all players order by height

select * from player order by height -- sort by ascending order


select * from player order by height desc -- sort by descending order


