def ordinal_suffix(number):
    """
    find out the suffix of any ordinal number
    :param number: natural number
    :return: suffix of the ordinal number
    """
    s = str(number)
    if s.endswith('11') or s.endswith('12') or s.endswith('13'):
        return 'th'
    elif s.endswith('1'):
        return 'st'
    elif s.endswith('2'):
        return 'nd'
    elif s.endswith('3'):
        return 'rd'
    return 'th'


'''
### if you put 1 / 2 / 3 check in the first place, 11 / 12 / 13 check will be ignored.
As any number ends with 11 also ends with 1, any number ends with 1 doesn't necessarily end with 11
'''


# generate_ordinal_str function calls 2 functions:
# 1) built-in function: str constructor
# 2) user-defined function: ordinal_suffix(number)
def generate_ordinal_str(number):
    """
    return the ordinal number
    :param number: the natural number
    :return: the ordinal number
    """
    return str(number) + ordinal_suffix(number)


# Another benefit of function: hide implementation, maybe user doesn't care.
# call function generate_ordinal_str
for i in range(1, 101):
    print(generate_ordinal_str(i))
