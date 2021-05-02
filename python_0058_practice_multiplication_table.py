'''
LOGIC:
1 there are total 9 lines
2 in each line, there are very similar items
     in 1 row,there is 1 item
     in 2 row,there is 2 item
     in 3 row,there is 3 item
     for each row,i loop in range(1,i+1):

'''
for r in range(1,10):
    for index in range(1,r+1):
        print(f'{index} * {r} = {index*r}',end=' ')
    print('')







