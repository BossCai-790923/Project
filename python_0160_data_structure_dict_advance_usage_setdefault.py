names = ['Ringo', 'Paul', 'John', 'Ringo', 'Ringo', 'John']
'''
requirement: 
i have a list of names. I want to know how many times each name appears.
'''
count = {}
for name in names:
    # traditional way -----
    # if name not in count:
    #     count[name] = 0

    # setdefault way --------
    count.setdefault(name, 0)

    # importance---------------
    # count.setdefault(name, 0) will add key / value pair (name, 0) IF key name doesn't exist in dict count
    # -------------------------
    count[name] += 1

print(count)