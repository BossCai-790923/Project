a_list = []
# a_list[4] = 'Tom' # IndexError: list assignment index out of range
# I try to assign the string 'Tom' to postion 4 in an empty list
# clearly impossible because that position 4 does not exist yet.

a_list = [None] * 5
print(a_list)
a_list[4] = 'Tom'
print(a_list)

a_dict = {}
a_dict[4] = 'Tom'
print(a_dict)

# important-------------------------------------------
# 4 in list is index;,list is order by index
# 4 in dict is key
# ----------------------------------------------------------

print(f'does value "Tom" exist in a_list? {"Tom" in a_list}')
print(f'does key "4" exist in a_dict? {"4" in a_dict}')
