#Requirement:calc the sum from1-100
sum_var_for_sl1=0
#sl1
for i in range(1,101):
    sum_var_for_sl1+=i
print(f'sum 1-100 is {sum_var_for_sl1} ')
#sl2
sum_var_for_sl2=sum(range(1,101))
print(f'sum 1-100 is {sum_var_for_sl1} ')
