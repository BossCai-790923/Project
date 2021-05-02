#requirement:mimic online game_user login
#def multi_line str variable as the welcome message
welcome_msg = '''
***************************
* WELCOME to King of Glory*
***************************
'''
print(welcome_msg)
user_name = input('User name:')
password = input('password:')
print(f'welcome, {user_name} , you"ve successfully logged in the game.')
total_coins = 0
run_out_of_coins_warn = f'Unfortunately,you have only {total_coins} coins in your account. please TOP UP Your account'
print(run_out_of_coins_warn)

coins_top_up = float(input('total coins to top UP :'))#conv str// to int


if coins_top_up < 0:
    print(f'you cannot top up {coins_top_up}.')
elif coins_top_up <=500:
    print(f'you top up {coins_top_up},you do not have enough coins')
    total_coins=coins_top_up+total_coins
elif coins_top_up == 500:
    total_coins += coins_top_up
else:
    print(f'you top up {coins_top_up},you can continue to play games')
    total_coins += coins_top_up

