scores=[85,96,77,68]
#reverse a list
scores.reverse()
print(scores)
print('/////////////////////////////////////////////////////')
#sort
#1 built in function-sorted()
sorted_scores=sorted(scores)
print(sorted_scores)
# ctrl alt v -> create new varable
sorted_scores_reverse=sorted(scores,reverse=True)
print(sorted_scores_reverse)
print(scores)
# built-in function: sorted(my_list) will create a [NEW] list with my_list's sorted values.
# my list is intact.

#2 methond sort()
scores.sort()
print(scores)
scores.sort(reverse=True)
print(scores)
# my list .sort() will sort the value in my list
# my list is changed