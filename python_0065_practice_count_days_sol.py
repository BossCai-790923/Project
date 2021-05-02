'''
Requirement:
Redo 0055 Using list
Requirement of 0055:
user inputs year / month / day information from the console
Your program needs to tell the user how many days in the year there are in front of the date which user input
For example: if user tells you 2019 Jan 1st, then your output should be 1
For example: if user tells you 2019 Feb 1st, then your output should be 32
'''

'''
Logic:
Observation:
For each date which user has typed in console, there are always fixed number of full months in front of the date.
For example:
there are always 4 full months in any date in May.
there are always 8 full months in any date in Sep.
Conclusion:
I can build a list - dayList, which contains 12 values. And these 12 values map Jan/Feb...Dec.
Each value stands for the total days' count for those full months in front the month.
dayList[0] = 0 # there are 0 days in those full months in front of any Jan date.
dayList[1] = 31 # there are 31 days in those full months in front of any Feb date.
dayList[2] = 31 + 28 # there are 31 + 28 days in those full months in front of any Mar date. (Ignore the leap year)
dayList[3] = 31 + 28 + 31 # there are 31 + 28 + 31 days in those full months in front of any Apr date.
... ...
the last step is just to plus the day of the date.
'''
print('please input as int. such as 2019 12 29')
years=int(input('years'))
month=int(input('month'))
days=int(input('days'))

daylist=[0,
         31,
         31+28,
         31+28+31,
         31+28+31+30,
         31+28+31+30+31,
         31+28+31+30+31+30,
         31+28+31+30+31+30+31,
         31+28+31+30+31+30+31+31,
         31+28+31+30+31+30+31+31+30,
         31+28+31+30+31+30+31+31+30+31,
         31+28+31+30+31+30+31+31+30+31+30,]
total=daylist[month-1]
total+=days
lpyear=False
if years%400==0 or (years%4==0 and years%100!=0):
    lpyear=True
if lpyear and month > 2:
    total+=1
print('total:',total)