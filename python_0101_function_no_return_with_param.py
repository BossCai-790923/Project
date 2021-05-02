"""
------------------------------
Pass Information to a function
------------------------------
Q) What is inside function parentheses?
A) You can define a variable which is only valid inside the function body.
   So here, you learn another way to define variable.
Q) What is Parameter?
A) Because the variable is ONLY valid inside the function body, so the variable has a special name - parameter
Q) Who will assign value to the variable(the parameter)?
A) When you call the function, you pass the value to the function call.
"""


# Define a function :greet user(username)####
def greet_user(username):
    """
    greet user,greet the specified user.
    :param username: Who you will greet
    :return: N o t h i n g
    """
    print(f'hello,{username}!')
    print("what a nice day!")
    print("nice to meet you on this beautiful weekend morning!")
    print("any plan today? i wish you have a good rest. after all, tomorrow is monday again.")


# call a function greet_user(username) ###
greet_user('Tom')
greet_user('Bitcoin')
greet_user('Doge_coin')
'''
Q) What is argument? 
A) When you call the function greet_user('Tom'), you put a str value 'Tom' in the pair of parentheses
   We say, you 'pass' value 'Tom' to the function greet_user('Tom')
   When the control goes inside the function body, this str value 'Tom' becomes the value of 
   the parameter(variable) 'username'

   Here, 'Tom' has a special name - argument
'''
