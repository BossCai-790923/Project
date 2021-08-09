dict1 = {'A': 80, 'B': 95}
dict2 = {'B': 90, 'C': 95}
'''
requirement:
i have 2 dict - dict1 & dict2.
i want to merge dict2 into dict1, then dict1 and dict2 becomes 1 dict.
possibly, some key / value pair in dict2 will override those in dict1
'''
print(f"Original dict1: {dict1}")

# solution1_____________________
# for key,value in dict2.items():
#   dict1[key}=value

# solution2______________________
dict1.update(dict2)

print(f"New dict1: {dict1}")