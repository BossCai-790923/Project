import numpy as np


def rabbit(month):
    if month <= 2:
        return 2
    else:
        return rabbit(month - 3) + rabbit(month - 1)



month = int(input("请输入month："))
for i in range(0, month):
    print(rabbit(i))