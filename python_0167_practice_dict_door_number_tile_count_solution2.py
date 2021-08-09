'''
There is big resort, it has 2000 rooms.
Door number tiles need to be installed for all these 2000 rooms, starting from '0001' to '2000'.
Door number is composed of 4 tiles. i.e.
'0001' is composed of 3 '0' and 1 '1';
'2000' is composed of 3 '0' and 1 '2'.
Question:
How many tiles need to be prepared for number 0 - 9?
'''

number_count_dict = {}
for number in range(10):
    number_count_dict[number] = 0

for doorplate in range(1, 2001):
    unit_digit = doorplate % 10
    ten_digit = (doorplate - unit_digit) // 10 % 10
    hundred_digit = (doorplate - ten_digit * 10 - unit_digit) // 100 % 10
    thousand_digit = (doorplate - hundred_digit * 100 - ten_digit * 10 - unit_digit) // 1000 % 10

    number_count_dict[unit_digit] += 1
    number_count_dict[ten_digit] += 1
    number_count_dict[hundred_digit] += 1
    number_count_dict[thousand_digit] += 1

print(number_count_dict)
