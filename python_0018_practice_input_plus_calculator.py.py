num1 = float(input('first num:'))
what_to_do = input('+ or - or x or "/" or "**":')
num2 = float(input('second num:'))
if what_to_do == '+':
    result = num1 + num2
    print(f'Result of {num1} + {num2} = {result}')
elif what_to_do == '-':
    result = num1 - num2
    print(f'Result of {num1} - {num2} = {result}')
elif what_to_do == 'x':
    result = num1 * num2
    print(f'Result of {num1} x {num2} = {result}')
elif what_to_do == '/':
    try:
        print(num1/num2)
    except ZeroDivisionError:
        print("You can't divide by zero!" )
    else:
        result = num1 / num2
        print(f'Result of {num1} / {num2} = {result}')
elif what_to_do == '**':
    result = num1 ** num2
    print(f'Result of {num1}**{num2} = {result}')