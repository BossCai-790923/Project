print('and rule')
print(f'True and True is{True and True}')
print(f'True and False is{True and False}')
print(f'False and True is{False and True}')
print(f'False and false is{False and False}')

print('or  rule__________________________________')
print(f'True or True is{True or True}')
print(f'True or False is{True or False}')
print(f'False or True is{False or True}')
print(f'False or false is{False or False}')

print('not rule -___________________________________')
print(f'not True is{not True}')
print(f'not False is{not False}')

bool_a = True
bool_b = False
bool_c = True
bool_d = False


# and - any value is False, then whole boolean expression is False
print(bool_a and bool_b and bool_c and bool_d)

# or - any value is True, then whole boolean expression is True
print(bool_a or bool_b or bool_c or bool_d)


# or - lowest priority, so it equals to
# bool_a and bool_b  or  bool_c and bool_d
print(bool_a and bool_b or bool_c and bool_d)



# So you use parenthesis () to change to evaluation order, so this equals to
# bool_a    and  bool_b or bool_c)       and       bool_d
print(bool_a and (bool_b or bool_c) and bool_d)


# not - highest priority, so it equals to
# bool_a    and  bool_b or bool_c)       and       not bool_d
print(bool_a and (bool_b or bool_c) and not bool_d)