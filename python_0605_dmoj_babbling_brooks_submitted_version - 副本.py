n = int(input())
rivers = []

for i in range(n):
    rivers.append(int(input()))

while True:
    command = int(input())
    if command == 77:
        break
    elif command == 99:
        index = int(input()) - 1
        percentage = int(input())
        left = rivers[index] * percentage / 100
        right = rivers[index] - left
        rivers[index] = left
        rivers.insert(index + 1, right)

    elif command == 88:
        index = int(input()) - 1
        rivers[index] = rivers[index] + rivers[index + 1]
        rivers.pop(index + 1)

for i in rivers:
    print(i, end= ' ')


# step 1) prepare data -------------------
n = int(input())

rivers = []

for i in range(n):
    rivers.append(int(input()))


# Step 2) mimic the process ---------------

while True:

    command = int(input())

    if command == 77:
        break

    elif command == 99:

        index = int(input()) - 1

        percentage = int(input())

        left = rivers[index] * percentage / 100
        right = rivers[index] - left

        rivers[index] = left
        rivers.insert(index + 1, right)


    elif command == 88:

        index = int(input()) - 1

        rivers[index] = rivers[index] + rivers[index + 1]

        rivers.pop(index + 1)


# Step 3) print the result ----------------------
for i in rivers:
    print(i, end= ' ')



'''
IMPORTANCE!!! ------------------------------
1) insert v into list: rivers.insert(index, v)
--------------------------------------------
'''