x = 2

def print_msg():

    # global tells python:
    # I am not defining any new variable.
    # x is a global scope variable
    global x

    x = x + 2
    print(x)

print_msg()