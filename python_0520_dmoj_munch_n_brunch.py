'''
https://dmoj.ca/problem/ecoo17r1p1
'''

price = [12, 10, 7, 5]

for trip in range(10):

    trip_cost = int(input())
    percent = input().split()
    students_total = int(input())

    students_list = []

    for i in range(4):
        students_list.append(int(float(percent[i]) * students_total))


    students_total_actual = sum(students_list)
    index = students_list.index(max(students_list))
    if students_total_actual > students_total:
        students_list[index] -= (students_total_actual - students_total)
    if students_total_actual < students_total:
        students_list[index] += (students_total - students_total_actual)



    proceeds = 0
    for i in range(4):
        proceeds += students_list[i] * price[i]

    after_cost = proceeds / 2

    print("YES" if after_cost < trip_cost else "NO")