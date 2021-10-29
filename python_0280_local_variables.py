

# local variable local_a is defined inside function example(), so it is NOT visible outside example()

#Python sees you are using variable local_a
# Firstly, Python tries to see whether local_a has been defined inside the current scope - example()
# Find it!
def example():

    local_a = 'Hello Python!' # scope: example()

    print(local_a)



example()

print("hello")

# variable local_a is NOT visible outside the function example()
# print(local_a)