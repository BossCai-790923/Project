'''
Requirement:
Find all 3 number combination possibilities for number 1, 2, 3, 4, 5

Your program should output all 10 possibilities, as below:
There are total 10 groups. They are:

 (1, 2, 3), (1, 2, 4), (1, 2, 5)
 (1, 3, 4), (1, 3, 5)
 (1, 4, 5)

 (2, 3, 4), (2, 3, 5)
 (2, 4, 5)

 (3, 4, 5)
'''

# I define a set to hold the 5 numbers
number_set = set(range(1, 6))
print(number_set)

# I define another set to hold all the combinations
# Why I use a set here? Because a set doesn't allow duplicate values
final_result_container = set()

for i in number_set:
    for j in number_set:
        for k in number_set:

            set1 = {i, j, k}

            # if i != j and i != k and j != k:
            if len(set1) == 3:  # ( diffrence ->len3)

                # set doesn't allow mutable values, like set,dict,list
                # set only allows immutable values, like int,float,bool,str,tuple
                # so I have to convert set1 to tuple
                tuple1 = tuple(set1)

                final_result_container.add(tuple1)

print(f"There are total {len(final_result_container)} groups. They are : {final_result_container}")

'''
HOMEWORK =============================================
Requirement:
Find all 3 number permutation possibilities for number 1, 2, 3, 4, 5
'''



number_set = set(range(1, 6))
print(number_set)

final_result_container = set()

for i in number_set:
    for j in number_set:
        for k in number_set:

            set1 = [i, j, k]

            if i != j and i != k and j != k:

                tuple1 = tuple(set1)

                final_result_container.add(tuple1)

number_set = set(range(1, 6))
print(number_set)


for i in number_set:
    for k in number_set:
        for j in number_set:

            set1 = [i, j, k]

            if i != j and i != k and j != k:

                tuple1 = tuple(set1)

                final_result_container.add(tuple1)



print(f"There are total {len(final_result_container)} groups. They are : {sorted(final_result_container)}")
