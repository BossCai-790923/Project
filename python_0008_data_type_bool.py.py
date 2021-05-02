#BOOL THE 4TH DATA TYPE IN PYTHON
#def variabes
bool1 = True#boo has only true or false
bool2 = False
print('variable bool type is:', type(bool1), 'bool1 =', bool1)
print('variable bool type is:', type(bool2), 'bool2 =', bool2)
#type tells you type of varabes
#bool1 and bool2 are type of 'bool'
bool3 = (1>2)#false
bool4 = (100<200)#true
print('variable bool type is','bool3=',type(bool3),bool3)
print('variable bool type is','bool4=',type(bool4),bool4)

#exp 1
# def variable toms_age
#toms_age == 20' is a boolean expression
tom_age = 20
print('is toms age 20?',tom_age == 20)
print('is tom 13 years old?' ,tom_age == 13)#false
print("Tom is not 20 years old.Isn't he?", tom_age != 20) #false
a = (tom_age == 20) # toms_age == 20 equals to true.
b = (tom_age == 13) # toms_age == 13 equals to false.
c = (tom_age != 20) # variable c equals to false
d = (tom_age != 13) # variable d equals to true
e = (tom_age < 20) # variable e equals to false
f = (tom_age <= 20) # variable f equals to true
g = (tom_age > 20) # variable e equals to false
h = (tom_age >= 20) # variable f equals to true
print(a,b,c,d,e,f,g,h) # True False False True False True False True
# TRASH TYPING
#a = tom_age == 20
#b = tom_age == 13
#c = tom_age != 20
#d = tom_age != 13
#e = tom_age < 20
#f = tom_age <= 20
#g = tom_age > 20
#h = tom_age >= 20

#EXP 2
my_math_mark = 75
is_my_mk_excellent = (my_math_mark>=90)
is_my_mk_fail = (my_math_mark<=60)
print('is_my_mk_fail',is_my_mk_fail)
print('is_my_mk_excellent?',is_my_mk_excellent)
booloop_mark = 75
bolloop_mark_same_as_me = (my_math_mark == booloop_mark)
print('bolloop_mark_same_as_me?',bolloop_mark_same_as_me)


