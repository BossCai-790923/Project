# merge
list_a = []
list_b = []
# to list_ab
# merge
list_c = [1, 5, 7]
list_d = [2, 2, 6, 8, 16, 17, 18, 19, 99]
# to list_cd
# merge
list_e = []

list_f = [2, 2, 6, 8, 16, 17, 18, 19, 99]
# to list_ef

new_list = []
index_a = 0
index_b = 0
# while True:
#     if list_a[index_a] >= list_b[index_b]:
#         new_list.append(list_b[index_b])
#         index_b += 1
#
#     elif list_a[index_a] < list_b[index_b]:
#         new_list.append(list_a[index_a])
#         index_a += 1
#     if index_a == len(list_a):
#         new_list.extend(list_b[index_b:])
#         break
#     if index_b == len(list_b):
#         new_list.extend(list_a[index_a:])
#         break
#
# print(new_list)
while list_a != [] or list_b != []:
    if index_a == len(list_a) and index_b < len(list_b):
        new_list.extend(list_b[index_b:])
        break
    if index_a < len(list_a) and index_b == len(list_b):
        new_list.extend(list_a[index_a:])
        break

    if list_a[index_a] < list_b[index_b]:
        new_list.append(list_a[index_a])
        index_a += 1
    else:
        new_list.append((list_b[index_b]))
        index_b += 1
print(new_list)