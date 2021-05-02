l=[]
i=0
print('input "exit" to quit')
while True:
    exit = input('Do you want to exit?')
    if exit != 'exit':
        n=input('next number')
        l.append(n)
        l.sort()
    print(l)


