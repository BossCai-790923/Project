'''
'''
'''
Logic
x * j = a*b
x   j
1   1
1   2
2   2
'''
x=1
j=1
ctrl='\n'
ctrl_x=1
ctrl_j=1
for i in range(9):
    if ctrl_x>j:
        ctrl_x=1
    x=ctrl_x
    j=ctrl_j
    print(x,'*',j,'=',x*j,sep='',end=ctrl)
    if x==j:
        ctrl='\n'
    if x!=j:
        ctrl=' '
    if j>x:
        continue
    ctrl_x=j
    ctrl_x+=1
    j+=1

    ctrl_j+=1