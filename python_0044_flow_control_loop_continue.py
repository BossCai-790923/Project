a=0
print('start')
#continue will return to the biggining of the LOOP
#it will ignore all statement behind him(in this loop)
while a < 5:
    a+=1
    if a == 3:
        continue
    print(a)
print('ends')