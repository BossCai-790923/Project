fl_a = float(input('number a : '))
fl_b = float(input('number b : '))
operator = input('operator:')
result  = 0

#inportance__________________________________
#if elif else review
#1!there is nothing after':'
#   after you type ':' press "enter'
#   pycharm will help you indent 4 space
#2!'elif' means else if . python make it short,just elif'
#inportance__________________________________
if operator == '+':
    result  = fl_a+fl_b
elif operator == '-':
    result  = fl_a-fl_b
elif operator == '*':
    result = fl_a * fl_b
elif operator == '/':
    if fl_b == 0:
        print('wrong input')

    else:
        result  = fl_a/fl_b
elif operator == '**':
    result  = fl_a**fl_b
else:
    print(f'unrecongnized operator {operator}')
    result = 0
print(f'{fl_a} {operator} {fl_b} = {result:.2f}')


