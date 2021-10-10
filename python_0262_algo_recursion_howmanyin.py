def howmanyin_once(target_list):
    return len(target_list)
'''
Summary:
1) Recursion is to convert the problem into a smaller scale sub-problem.
howmanyin(target_list) is converted to 1 + howmanyin(target_list[1:])
'''

def howmanyin(target_list):

    if len(target_list[1:])!=0:
        return 1+howmanyin(target_list[1:])

    else:
        return 1

l1=[]
for n in range(10):
    l1.append(n)

print(f'list size is {howmanyin(l1)}')