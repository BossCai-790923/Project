tuple_1 = 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b'
# ----------------------------
# index(value) finds the index of the 1st appearance of the value
index_of_a = tuple_1.index('a')
print(index_of_a)
# -------------------------
#index(value, begin_index) finds the index of the 1st appearance of the value AFTER index 'begin_index'
index_of_a = tuple_1.index('a', index_of_a + 1)
print(index_of_a)
# ----------------------
index_of_a = tuple_1.index('a', index_of_a + 1)
print(index_of_a)