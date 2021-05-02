age = 15
if age < 18:
    kids_or_adult = 'kids'
else:
    kids_or_adult = 'adult'

#simp:
kids_or_adult = 'kids'  if age<18 else 'adult'

#IMPORTANT________________________________________________________
#<value when True> if <boolean expression> else <value when false>
#IMPORTANT________________________________________________________

#exp2!
fruit = 'apple'
isapple = True if fruit == 'apple' else False
#exp3!
x = 18
result = 'high' if x > 10 else 'low'