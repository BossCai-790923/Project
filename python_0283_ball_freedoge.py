def freeeeeeeball(times):
    height=100
    totalmoves=0


    for i in range(times):
        totalmoves+=(1/2)*totalmoves
        height=(1/2)*height
    print(totalmoves)
    print(height)


freeeeeeeball(10)