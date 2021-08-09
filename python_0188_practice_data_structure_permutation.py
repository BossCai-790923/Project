number_set = set(range(1, 6))
# print(number_set)

final_result_container = list()

for i in number_set:
    for j in number_set:
        for k in number_set:
            if i != j and i != k and j != k:
                tuple1 = (i, j, k)
                final_result_container.append(tuple1)

print(f"There are {len(final_result_container)} groups. they are: {final_result_container}")