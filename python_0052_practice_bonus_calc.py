'''


# Requirement:
# You receive a email from NTUC Supermarket CEO Mr Seah.
# Good Morning!
# It is the end of the year 2020. Time flies! I need you to help develop a program which is to calculate how much bonus we should pay to all our staff
# as their end of year bonus. Here is my basic idea:
# We need to distribute the total bonus to all our staff based on the supermarket's yearly performance.
# We plan to calculate the total bonus using a layered strategy. Specifically:
# 1) If the supermarket's yearly profit is less than 1 million, then
#    i) 10% of the profit will be used as the total bonus.
# 2) If the supermarket's yearly profit is less than or equals to 2 million, then the total bonus is composed of
#    i) 10% of the 1st million profit
#    ii) 7.5% of the remaining profit
# 3) If the supermarket's yearly profit is less than or equals to 4 million, then the total bonus is composed of
#    i) 10% of the 1st million profit
#    ii) 7.5% of the 2nd million profit
#    iii) 5% of the remaining profit
# 4) If the supermarket's yearly profit is less than or equals to 6 million, then the total bonus is composed of
#    i) 10% of the 1st million profit
#    ii) 7.5% of the 2nd million profit
#    iii) 5% of the 3rd and 4th million profit
#    iv) 3% of the remaining profit
# 5) If the supermarket's yearly profit is less than or equals to 10 million, then the total bonus is composed of
#    i) 10% of the 1st million profit
#    ii) 7.5% of the 2nd million profit
#    iii) 5% of the 3rd and 4th million profit
#    iv) 3% of the 5th and 6th million profit
#    v) 1.5% of the remaining profit
# 6) If the supermarket's yearly profit is above 10 million, then the total bonus is composed of
#    i) 10% of the 1st million profit
#    ii) 7.5% of the 2nd million profit
#    iii) 5% of the 3rd and 4th million profit
#    iv) 3% of the 5th and 6th million profit
#    v) 1.5% of the 7th, 8th, 9th and 10th million profit
#    vi) 1% of the remaining profit
# So when the program starts, I, as the CEO of the supermarket can input the total profit of the year, then you program will
# tell me how much bonus I should keep for our staff.
# Another thing is, as you know, we have in total 230 outlets in the whole island.
# So you program should be able to run repetitively, asking me to input the total profit of some outlet, then tell me the bonus number for that outlet, until I say 'exit'.
# This is a critical program as it is related to the money. Please make sure your program can calculate the correct amount.
# I trust you can do this job beautifully as a seasoned python programmer.
# Good luck!
# Mr.Seah

'''
while True:
    profit_str=input('total profit of the year: ')
    if profit_str=='exit':
        break
    profit = int(profit_str)
    bonus = 0
    if profit<=1000000:
        bonus=profit*0.1
    elif profit<=2000000:
        bonus=1000000*0.1
        bonus+=(profit-1000000)*0.075
    elif profit <= 4000000:
        bonus=1000000*0.1
        bonus+=1000000*0.075
        bonus+=(profit-2000000)*0.05
    elif profit <= 6000000:
        bonus = 1000000 * 0.1
        bonus += 1000000 * 0.075
        bonus+= 2000000 * 0.05
        bonus += (profit - 4000000) * 0.03
    elif profit <= 10000000:
        bonus = 1000000 * 0.1
        bonus += 1000000 * 0.075
        bonus+= 2000000 * 0.05
        bonus+=4000000*0.03
        bonus += (profit - 6000000) * 0.015
    else:
        bonus = 1000000 * 0.1
        bonus += 1000000 * 0.075
        bonus += 2000000 * 0.05
        bonus += 4000000 * 0.0015
        bonus += (profit - 10000000) * 0.01
    print(f'we should keep ${bonus} to our staff for this outlet.')


