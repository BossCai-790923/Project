l=[]
i=0
n=[]
while True:
    print('input "exit" to quit')
    exit=input('Do you want to exit?')
    if exit != 'exit':

        yz=int(input('how many do you want'))


        for i in range(yz):
            x=float(input('input a number :'))
            n.append(x)


        if exit !='exit':
            for i in range(yz):
                min_n=min(n)
                l.append(min_n)
                n.remove(min_n)




            print(l)
            n.clear()


    else:
        break

