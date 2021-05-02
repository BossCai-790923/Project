#requirement:Print out str'my name is bond, James Bond' using var 'first name' and 'last name'
first_name = 'James'
last_name = 'Bond'

#[sol 1] pass 4 str values to Print() function
#problem there is a extra space between bond and ','
print('My name is',last_name,',',first_name,last_name)#My name is Bond , James Bond

#[sol2] Use '+' to connect 6 str^ together,pass the newly joined str value to print() function
#problem very messy not readable
print('My name is ' + last_name + ', ' + first_name + ' ' + last_name) #My name is Bond, James Bond

#[sol3] python f' string
#ImPorTanCe----------------------------------------------------------------------------
#1] have an f at the beginning
#2] curly braces containing expressions that will be replaced with their values
#--------------------------------------------------------------------------------------
print(f'my name is {last_name}, {first_name} {last_name}')

#more Examples
print(f'Nooooo,"Mr"{last_name},I expect you to d&%')

age = 90
print(f'Sean Connery is now {age} years old')

language = 'Python'
rank = 1
who = 'all students'
kids_age = 13
teacher_surname = 'Tom Fan'
print(f'{language} is the world no {rank} programming language, {who} should start learning it from age {kids_age} years old.')
print(f'And they all learn {language} with Teacher {teacher_surname}.')
print(f'{who} enjoy learning {language}, as {language} is quite fun, and Teacher {teacher_surname} is quite fun. :)')