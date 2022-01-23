'''
Q) What's the greedy algo?
   a) do sth step by step
   b) at each step, choose the best choice, not worrying about the future.
   局部最优 (local optimal), 全局最优 (global optimal)
   c) after all steps finish, you get the best result.
   d) because you need to make a choice at each step, so quite often, you have a option list.
   e) because you need to make a best choice, so quite often, you need to sort the option list.
'''





'''
Q) Someone owes you $23.69 and gives you a hundred-dollar bill. How will you give him the changes?
'''

denomination = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 50]

owed = 76.31
payed = []

# # Step 1) sort the option list
# denomination.sort(reverse=True)
#
# # Step 2) try all the notes / coins 1 by 1
# for d in denomination:
#     while owed >= d:
#         owed -= d
#         payed.append(d)
#
# # Step 3) print the result
# print(sum(payed))
# print(payed)
#

'''
greedy algo doesn't always give you correct answer. 
coins = [1,4,5]
owed = 8
greedy payed = [5,1,1,1]
dp payed = [4,4] 
反例方法
'''
# denomination = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 50]
#
# owed = 76.31
# payed = []
#
# # # Step 1) sort the option list
i=-1
denomination.sort()
while True:
    if owed>denomination[i]:
        payed.append(denomination[i])
        owed-=denomination[i]
        if owed>denomination[i]:
            pass
        else:
            i-=1
    if sum(payed)==owed:
        break


print(sum(payed))
print(payed)