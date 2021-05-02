#you cant do the follow in g 2 things at the time:
#1 loop a list
#2 add value to the list/remove value from the list

#don't loop and modify.
'''

'''
'''
requirement
create a list from str |python|,
loop all the letter in you new list.
if uou meet letter 't':remove it from your list
otherwise:print the letter to console
'''

l1=list('PYTHON')

for ch in l1:
    if ch == 'T':
        l1.remove(ch)
    else:
        print(ch)

# IMPORTANT !!! -------------------------
# What I expect: the program prints 'p', 'y', 'h', 'o', 'n'
# What I see   : the program prints 'p', 'y', 'o', 'n'
# Problem      : 'h' is missing.
#
# Root cause:
# 1) Long story short: list values' index are updated.
# 2) Detailed explanation:
#
#    --------------------------
#    | P | y | t | h | o | n |
#    --------------------------
#    | 0 | 1 | 2 | 3 | 4 | 5 |
#    --------------------------
#
# Because Python loop your list1 by index, so it loops from 0 to 5.
# When Python loops to 't', Python remembers, 'I am looping index 2, now, next I should loop index 3.
# Then you remove 't', so 'h', 'o', 'n' index change to '2', '3', '4'
# So python ignore 'h', next round, python handles 'o'
# ------------------------------------------


# IMPORTANT !!! -------------------------------------------------
# Solution: You loop a copy of your original list. So that you don't 'loop and modify'
# ---------------------------------------------------------------

print("---------------------------------------")


list1 = list("Python")

for ch in list1[:]:
    if ch == 't':
        list1.remove(ch)
    else:
        print(ch)