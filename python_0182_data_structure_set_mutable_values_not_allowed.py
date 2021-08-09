int_Set={1,2,3}
print(int_Set)
str_set={'1','2','3'}
print(str_set)
bool_set={True,False}
print(bool_set)
tuple_set={(1,2),(3,4)}
# list_set = {[1, 2], [3, 4]} # TypeError: unhashable type: 'list'
# print(list_set)
#
# dict_set = {{1:2}, {3:4}}   # TypeError: unhashable type: 'dict'
# print(dict_set)
#
# set_set = {{1, 2}, {3, 4}}  # TypeError: unhashable type: 'set'
# print(set_set)

# IMPORTANCE !!! -----------------------------------
# 1) mutable values (list, dict, set) are not allowed in set
# 2) immutable values (int, float, bool, str, tuple) are allowed in set.
#
# Reason:
# You can change the elements' value to be the same after they are in the set already.
# This will break set's rule - no same elements are allowed in set
# --------------------------------------------------
