'''
requiement
ask user to input a number from Console
then you need to tell wheather the number is a square number or not
'''

# get user input
number_a = int(input('please input a number'))

# core logic
# 5**2 = 25
# 5**3 = 125
# 5**4-625
# 25**(1/2)=5
# 125**(1/3)=5
# 625**(1/4)=5
# --------------
number_a_sq_rt = number_a**(1/2)
print(f'{number_a} square root is {number_a_sq_rt}')

number_a_sq_rt_int = int(number_a_sq_rt)
print(f'after i convert{number_a_sq_rt} to int , its value is{number_a_sq_rt_int}')
if number_a_sq_rt == number_a_sq_rt_int:
    print(f'because {number_a_sq_rt} == {number_a_sq_rt_int}, so {number_a} is a square number')
else:
    print(f'because {number_a_sq_rt} != {number_a_sq_rt_int}, so {number_a} is not a square number')

# secret knowledge ___________________________
# please try replace all
# number_a_sq_rt
# to
# number_a_sq_rt:.2f
#
# :.2f has 3 parts:
#
# :       means I want format this number_a
# .2      means keep 2 digits after the decimal point.
#  f      means this is float number_a
# _____________________________________________
