number_list = list(range(100))
print(number_list)

# Requirement 1 Use slice generate list 10,11,12 ... 20
# Requirement 2 Use slice generate list 1,3,5,7,9 ... 99
# Requirement 3 Use slice generate list 9,11,13,15 ... 49
# Requirement 4 Use slice generate list 98,96,94,92 ... 0
# Requirement 5 Use slice generate list 50,48,46,44 ... 10
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
l1=list(number_list[10:21])
print(l1)
l2=list(number_list[1:100:2])
print(l2)
l3=list(number_list[9:50:2])
print(l3)
l4=list(number_list[-2:-100:-2])
print(l4)
l5=list(number_list[-50:-92:-2])
print(l5)