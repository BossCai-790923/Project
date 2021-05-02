print('please input as int. such as 2019 12 29')
years=int(input('years'))
month=int(input('month'))
days=int(input('days'))
all=0
mtd = 0
l=[]
#mtd=month to days
if years %4==0 and years % 100 != 0:
    print('leap year')
    if month >2:
        mtd+=1
if years %400 ==0:
    print('leap year')
    if month >2:
        mtd+=1

#month calc_________
if days != 0 and days < 32 and month != 0 and month < 13:

    if month==12:
        mtd+=30*11 + 1 +1+1+1+1+1-2
    if month==11:
        mtd+=30*10  +1+1+1+1+1+1-2
    if month==10:
        mtd+=30*9+1+1+1+1+1-2
    if month==9:
        mtd+=30*8+1+1+1+1+1-2
    if month==8:
        mtd+=30*7+1+1+1+1-2
    if month==7:
        mtd+=30*6+1+1+1-2
    if month==6:
        mtd+=30*5+1+1+1-2
    if month==5:
        mtd+=30*4+1+1-2
    if month==4:
        mtd+=30*3+1+1-2
    if month==3:
        mtd+=30*2+1-2
    if month==2:
        mtd+=30+1
    if month==1:
        mtd+=0
else:
    print('wrong input')
    all=0
    mtd=0
    days=0
all=mtd+days
print(all)