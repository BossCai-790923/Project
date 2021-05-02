'''
logic:
There are several boundaries in the question description:
1) 1 million            10%
2) 2 million            7.5%
3) 3rd / 4th million    5%
4) 5th / 6th million    3%
5) 7/8/9/10th million   1.5%
6) remaining            1%
The description can be converted to the table below:
        ====================
        threshold       rate
        ====================
        above			1%
        --------------------
        4 million		1.5%
        --------------------
        2 million		3%
        --------------------
        2 million		5%
  ^     --------------------
  |     1 million		7.5%
  |     --------------------
  |     1 million		10%
----------------------------------------------------------
as profit goes up, the percentage goes down for each tier.
'''

# Step 1) Define a variable profit - I read annual profit from console
total=0.0

# Step 2) Define variable bonus - use float constructor
bonus = 0.0

# Step 3) Define variable thresholds and rates which represent the table definition above.
rates = [0.1, 0.075, 0.05,0.05, 0.03,0.03, 0.015, 0.015,0.015,0.015,0.01]

# Then I use variable I defined above.
a=int(input('profit'))
x=0
# if a > 10000000:

if a >10000000:
    bonus+=395000
    a=a-10000000
    bonus+=a*0.01
    print(f'we should keep ${bonus} to our staff for this outlet.')
    exit()
if a <1000000:
    bonus=a*rates[0]
    print(f'we should keep ${bonus} to our staff for this outlet.')
    exit()
y=int(a/1000000)
for i in range(y):
    z=rates[i]*1000000
    bonus+=z
n=a%1000000
bonus+=(n*rates[y])
print(f'we should keep ${bonus} to our staff for this outlet.')
print(bonus)