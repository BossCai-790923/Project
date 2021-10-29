

# variable global_a is not defined inside any sub function, it is defined directly inside the module.
# so it is global variable.
# so it is visible everywhere.

global_a = "Hello Python!"

def example():

    # Python sees you are using variable global_a
    # Firstly, Python tries to see whether global_a has been defined inside the current scope - example() or not
    # Nope!
    # Secondly, Python tries to see whether global_a has been defined globally?
    # Find it!
    print(global_a)

example()