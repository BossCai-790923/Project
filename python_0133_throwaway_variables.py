buy_order = ('DBS', 100, 29.5, (2021, 5, 14, 10, 28, 7, 123))
# when unpacking, you may sometimes want to discard certain values.
# so you use underscore to represent, you don't need this value
_, shares, price, _ = buy_order
print(shares, price)

#another example:
#in my loop body ,I don't need this variable,so I just use'_'
for _ in range(10):
    print('hello,python')