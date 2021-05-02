##list can be nested
x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
print(x)

#agj
print(x[0],x[2],x[4])
#bb,ccc,ddd,ee,ff
print(x[1])

#bb
print(x[1][0])
#ee
print(x[1][2])
#ddd
print(x[1][1][1])
#ccc,ddd
print(x[1][1])
#ff
print(x[1][3])