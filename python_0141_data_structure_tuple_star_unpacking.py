# '''
# requirement:
# you have a long, sorted tuple, which contains the scores of the whole class.
# You need to remove the lowest_and the highest scores, and get an average score of the whole class.
# '''

grades = (55, 57, 60, 67, 77, 78, 79, 83, 85, 99, 100)

# solution 1) slice
middle_score = grades[1:-1]
print(type(middle_score))
print(sum(middle_score) / len(middle_score))

# solution 2) unpacking - star variable in the middle
lowest, *middle_score, highest = grades
print(type(middle_score))
print(sum(middle_score) / len(middle_score))


# example 2: unpacking a list -------------------------------------

# start variable in the last
record1 = ['dave', 'dave@hotmail.com', '91234567', '61234567', '81234567']
name_, email_, *phone_numbers = record1
print(phone_numbers)

record2 = ['billy', 'billy@hotmail.com']
name_, email_, *phone_numbers = record2 # unpacking here generates an empty list
print(phone_numbers)

record3 = ['dave', 'dave@hotmail.com', '91234567']
name_, email_, *phone_numbers = record3 # unpacking here generates a list which contains 1 value only
print(phone_numbers)



# example 3: use together with throwaway variable -----------------------

tuple_numbers = 1,2,3,4,5,6,7,8,10,100

lowest_, *_, highest_ = tuple_numbers
print(lowest, highest)

*_, second_high, first_high = tuple_numbers
print(second_high, first_high)

# ------
# summary
# -------
# 1) unpacking can be applied to either a tuple or a list
# 2) unpacking is very useful when you to try to group a part of a list / a tuple, into a new list
