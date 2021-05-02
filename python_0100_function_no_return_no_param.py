# we used to say:define a variable,use a variable
# now we say :define a function,call a function.
# Part 1) define a function: greet_user() --------------------------
#
# def          : keyword. Every time you define a function, you start with 'def'.
# greet_user   : function name. Just like variable name. Important: function name must be meaningful.
# ()           : parentheses.
# :            : Just like you use ":" at the end of a for range loop, it begins your function body.
def greet_user():
    """
    display a simple greeting.
    this part is called 'docstring'
    It tells you what he function does.
    if you move your mouse over the function name, you can see docstring appear.

    :return: Nothing...
    """
    print('hello')
    print("what a nice day!")
    print("nice to meet you on this beautiful weekend morning!")
    print("any plan today? i wish you have a good rest. after all, tomorrow is monday again.")


# part 2 call a function
greet_user()
greet_user()
greet_user()
greet_user()
greet_user()


# example 02 #
def launch_a_missile():
    """
    this function will launch a missile
    :return: Go Go GO!
    """
    print('Missile launched!!!!')


launch_a_missile()
launch_a_missile()
launch_a_missile()
