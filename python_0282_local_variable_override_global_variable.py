
str_a = 'Hello Python!' # scope: global


# I define a function with a parameter named str_a, which is the same as the global variable
# IMPORTANCE!! All parameters are actually variable you defined, with the function scope.
def print_msg1(str_a):
    # Python sees you are using variable str_a
    # Firstly, Python tries to see whether str_a has been defined inside the current scope - print_msg1() or not
    # Find it!
    print(f"I am using a local variable 'str_a': {str_a}")


print_msg1("Good day!")


def print_msg2():
    str_a = "Hello Singapore!"
    # Python sees you are using variable str_a
    # Firstly, Python tries to see whether str_a has been defined inside the current scope - print_msg2() or not
    # Find it!
    print(f"I am using a local variable 'str_a': {str_a}")


print_msg2()



def print_msg3():
    print(f"I am using a local variable 'str_a': {str_a}")

    # Python sees you are using variable str_a
    # Firstly, Python tries to see whether str_a has been defined inside the current scope - print_msg3() or not
    # Nope!
    # Secondly, Python tries to see whether str_a has been defined globally?
    # Find it!

print_msg3()

# Global variable is visible everywhere.
print(str_a)

