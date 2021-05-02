#req a costomer walks into pet's store,he want a
# male cat, white or yellow
# or a female cat,not white
# or just a black one
# you need input from consle gender and cat color
# tell costomer he wants or not
gender = input('gender:')
color = input('color of cat:')

#1> gender == male and (color == 'white' or color =='yellow')
#or
#2> gender == 'female' and not color == 'white'
#               also gender == 'female' and color != 'white'
#or
# 3> color == 'black'

if gender == 'male' and (color == 'white' or color =='yellow') or gender == 'female' and not color == 'white' or color == 'black':
    print(' I will take it')
else:
    print('I do not want it.')
