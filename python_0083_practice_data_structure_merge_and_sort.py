# merge
list_a = []
list_b = []

new_list = []
index_a = 0
index_b = 0
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