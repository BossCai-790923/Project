x = 2

def print_msg():

    '''
    python sees x = ...
    Python believes there are 2 situations:
    situation 1) You are defining a new variable
    situation 2) You are assiging a new value to an existing variable
    step 1) python needs to figure out, what is this x? Where is it defined?
    step 2) Python looks up x in the current scope (print_msg() method scope), not found.
    step 3) So you are defining a variable.
    Step 4) Python reads further, x = x + 2
    Step 5) Python is confused, why you are using x before you define x? This is error, I need to report it!
    '''
    # global x
    x = x + 2
    print(x)

print_msg()