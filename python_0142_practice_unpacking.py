def cooking(dish1, dish2):
    print(f"Start cooking: {dish1}")
    print(f"Start cooking: {dish2}")
def playing(game):
    print(f"Start playing: {game}")
def coding(language, type, deadline):
    print(f"Start coding {language} {type}, it should be finished by {deadline}")
# ------------------
# main program starts
# ---------------
actions = [
    ('cooking', 'fish', 'pork'),
    ('PLAYING', 'badminton'),
    ('coding', 'Python', 'homework', 'Sunday')
]
# actions is a list
# actions is a list of tuples
# each tuple contains variable number of values
'''
1) 'for loop' loops all the tuples in the actions list
2) each tuple will be unpacked into 2 variables:
   a) action, which is of str type, contains the 1st value of the tuple
   b) arguments, which is of list type due to the star in front of it. (This is what we learnt in 141)
   c) list arguments contains the remaining values of the tuple
'''
for action, *arguments in actions:
    '''
    You pass list arguments function cooking() / playing() / coding()
    function cooking() accepts 2 values.
    function playing() accepts 1 value.
    function coding() accepts 3 values.

    The * in front of the list arguments can 'unpack' the list arguments into individual values. (This is what we learnt in 117 / 118)
    '''
    if action == 'cooking':
        cooking(*arguments)
    elif action == 'playing':
        playing(*arguments)
    elif action == 'coding':
        coding(*arguments)