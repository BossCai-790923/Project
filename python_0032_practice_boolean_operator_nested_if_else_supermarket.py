'''
req
1 imp NTUC supermarket price calc

2 each time ,a customer buy a product beef/pork/tomato/apple/orange

3 beef / pork / tomato - total price calc by weight
    beef - $20 / kg
    pork - $16 / kg
    tomato - $5 / kg

4 apple / orange - total price calc by quantity
    apple - $5 for 5 apples; $1.6 each
    orange - $5 for 3 oranges; $2 each

5 imple ment a menbership system ,total price *0.9
    ask cstmr are you a member
    'y','Y','Yes','yes'means he(she) is a member
6 implement payment system which supports Visa/Mastercard/Nests/Cash
    if user pays visa/master card, need signature(input())
    if user pay with nets, ask user password(input())
    if user pays with cash ,check whether you should give him change or enougth money

'''

welcome_msg = '''
*********************************************
*       welcome to NTUC SUpermarket         *
*********************************************
'''
print(welcome_msg)

product_price = '''
______________________________________________________
beef - $20 / kg
pork - $16 / kg
tomato - $5 / kg
apple - $5 for 5 apples; $1.6 each
orange - $5 for 3 oranges; $2 each
'''

print(product_price)
unit_price = 0
how_many  = 0
less_five = 0
how_many_five = 0

product_name = input('what product do you want (beef/pork/tomato/apple/orange): ')

total_price = 0

if product_name == 'beef' or product_name == 'pork'  or product_name == 'tomato':

    total_weight = float(input('total weights in kg:'))

    if product_name == 'beef':
        unit_price = 20
    elif product_name == 'pork':
        unit_price = 16
    else:
        unit_price = 5
    total_price = unit_price * total_weight
    print(f'{product_name}:${unit_price} * {total_weight} == ${total_price}')

elif product_name == 'apple' or product_name == 'orange':
    how_many = int(input('(int) how many do you want???'))
    if product_name == 'apple':
        less_five = (how_many % 5)
        how_many_five = ((how_many - less_five) / 5 * 5)
        total_price += less_five*1.6 + how_many_five
        print(f'u buy {how_many} apple,total price is {how_many_five} + {less_five} *1.6 = {total_price}')
    if product_name == 'orange':
        less_three = (how_many % 3)
        how_many_three = ((how_many - less_three) / 3 * 5)
        total_price += less_three * 2 + how_many_three
        print(f'u buy {how_many} orange,total price is {how_many_three} + {less_three} *2 = {total_price}')

else:

    print(f'Unrecognized {product_name}')

give_money = 0
#member
member_str = input("Are you a member? ")

if member_str == 'Y' or member_str == 'y' or member_str == 'Yes' or member_str == 'yes':
    total_price *= 0.9
    print(f'After discount, total price: ${total_price}')

#pay ment
payment = input('Visa/Mastercard/NETS/Cash?')
if payment == 'Visa' or  payment == 'Mastercard':
    sign = input('signature here')
    print(f'signature{sign}is well received')
    print(f'{total_price} has been charged to your {payment} card')
elif payment == 'NETS':
    psd = input('password')
    print(f'{total_price}has been charged to {payment} card')
else:
    give_money = int(input('pay money : '))
    if give_money > total_price:
        print(f'Your change is {give_money - total_price:.3f}')
    elif give_money == total_price:
        print(f'nice costomer ,you pay {give_money} = {total_price}')
    else:
        print(f'{give_money} is not avaliable to buy. total price is {total_price},you need give me {total_price-give_money:.3f} more.')