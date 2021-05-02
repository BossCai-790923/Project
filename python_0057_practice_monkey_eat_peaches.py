'''
Requirement:
There is a group of monkeys who eat a pile of peaches.
On Day 1, they eat half plus 1
On Day 2, they eat half plus 1 again
...
On Day 10, they notice there is only 1 peach left before they eat.
Question:
1) How many peaches in total in Day 1?
2) Print out from Day 1, how many peaches in total? How many peaches they eat? How many peaches are left. Till last day.
'''

'''
code logic:
1) To calculate the 1st day, we have to calculate 9th day, 8th day, till 1st day.
    I should use for loop, loop in range(9,0,-1)

2) On each day there are 3 numbers:
   a) How many peaches in total at first?  define a new variable peach_total
   b) How many peaches the monkey eat?     define a new variable peach_eaten
   c) How many peaches are left?           define a new variable peach_left
   peach_total = peach_eaten + peach_left

3) On 10 day, before the monkey eat, they notice there is only 1 peach left      
   day 9:
   peach_left = 1
   peach_total = (peach_left + 1) * 2
   day 8:
   peach_left (day 8) = peach_total (day_9)
   peach_total = (peach_left + 1)
'''
peach_total=1
print(f'On 10 day, before the monkey eat, they notice there is only {peach_total} peach left ')
for day in range(9,0,-1):
    peach_left = peach_total
    peach_total=(peach_left+1)*2
print(f'on day 1,there are {peach_total} peaches before they eat')
print('__________________________________')

for i in range(1,10):
    peach_eaten=(peach_total//2)+1
    peach_left=peach_total-peach_eaten
    print(f'on day {i},there are {peach_total} peaches before they eat')
    print(f'tehy eat {peach_eaten} peaches')
    print(f'there are {peach_left} peaches left')
    peach_total=peach_left