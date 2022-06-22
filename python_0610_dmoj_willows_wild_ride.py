
for i in range(10):
    i, j = input().split()
    i = int(i)
    j = int(j)
    k = []

    for _ in range(j):
        t = input()
        if t == 'E':
            k.append(0)
        else:
            k.append(1)
    l = []
    for index, box in enumerate(k):
        day = index + 1
        if box == 0:
            if len(l) < day:
                l.append(0)
        else:
            l.extend([1] * i)

    print(len(l) - j)
