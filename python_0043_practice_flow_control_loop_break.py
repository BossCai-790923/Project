#req
#get user unput from constle ask to input number
#if it divide 7 and % =0
#print exit
#else:
#continue try again
while True:
    in_num = int(input('number: '))
    if in_num % 7 == 0:
        print(f'yes .{in_num}can divide by 7')
        break
    else:
        print(f'{in_num}is not divisible by 7.')
