All_Factor=[]
init=0
Prime_Factor=[]
for i in range(1,10001):
    if i > 1:
        for x in range(2,i):
            if i%x ==0:
                break
        else:
            Prime_Factor.append(i)
print(Prime_Factor)
def Factorization_prime_factor (num):
    if num != 0 and num != 1:
        for o in range(100000000000):
            for init in range(100):
                if num % Prime_Factor[init] == 0:
                    num /= Prime_Factor[init]
                    All_Factor.append(Prime_Factor[init])


                All_Factor.sort()
                print(All_Factor)
            
    else:
        print(f'{num} cannot be Factorization_prime_factored.' )

    print(All_Factor)
    All_Factor.clear()
while True:
    doge=int(input('Please input the int: '))
    Factorization_prime_factor(doge)
