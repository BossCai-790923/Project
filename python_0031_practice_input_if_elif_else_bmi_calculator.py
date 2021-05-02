# requirement: get input from the user about height in meters and weight in kg.
# calculate his bmi based on this formula:
# bmi = weight / (height ** 2)
# print information based on user's bmi value
# bmi in (0, 16)      : you are severely underweight
# bmi in [16, 18.5)   : you are underweight
# bmi in [18.5, 25)   : you are healthy
# bmi in [25, 30)     : you are overweight
# bmi in [30, max)    : you are severely overweight

height = float(input('enter in meters:'))
weight = float(input('enter weight in kg:'))
bmi = weight / (height ** 2)
print((f'your bmi is {bmi:.4f}'))

#IMP_________________________________________________________________-
#there is 2 ways to experss 'bmi' in range [16,18.5)
#s1     elif bmi >= 16 and bmi < 18.5:
#s2     elif 16 <= bmi < 18.5
#IMP_________________________________________________________________-
if bmi < 16:
    print('severely underweight')
elif 16 <= bmi < 18.5:
    print(' underweight')
elif 25 <= bmi < 30:
    print('you are overweight')
else:
    print('too fat (doge)')