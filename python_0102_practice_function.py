'''
Requirement 1)
Write a function called display_message() that prints one sentence telling everyone what you've learnt today.
Call the function, and make sure the message displays correctly.
Requirement 2)
Write a function called favorite_book() that accepts one parameter, title.
The function should print a message, such as One of my favorite books is Alice in Wonderland.
Call the function, making sure to include a book title as an argument in the function call
'''


def display_message(str):
    '''
    display message
    :param str:
    :return:
    '''
    print(str)


display_message("we've learned how to built function")


def favourite_book(str):
    '''
    print your favourite book
    :param book:
    :return:
    '''
    print('One of my favorite books is','"'+str+'"')


favourite_book('Scrolls For Success')
