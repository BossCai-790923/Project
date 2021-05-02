"""
Requirement 1)
Write a function called display_message() that prints one sentence telling everyone what you've learnt today.
Call the function, and make sure the message displays correctly.
Requirement 2)
Write a function called favorite_book() that accepts one parameter, title.
The function should print a message, such as One of my favorite books is Alice in Wonderland.
Call the function, making sure to include a book title as an argument in the function call
"""


def display_message():
    print('I"ve learnt how to define a function in python')


display_message()


def favorite_book(title):
    print(f'My favourite book is {title}')


favorite_book('Alice in wonderland')
