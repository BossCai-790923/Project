
#importance------------------------------------------------------------------
#
#if <boolean expreession>:
#   <statement>
#   <statement>
#   <statement>
#else:
#   statement
#   statement
#
#1,':' at end of else clause
#2,All code under else section are indented 4 spaces
#3,treat the 2 print statements under else clause as a 'block,because they indented 4 spaces
#   the 'block' will be executed if years learning python >5 is false or the block won't get executed
#----------------------------------------------------------

#if years_learning_python == 5
#then 5>5 is false

years_learning_python = int(input('how many years have you been learning Python?'))
if years_learning_python > 5:
    print(f'not bad!{years_learning_python}years is quite a long time , you`ve already been a python Guru.')
    print('I am sure you can earn lot of money in the market!')
else:
    print(f'{years_learning_python} years is still quite a short time.')
    print('i know sit is hard,just hang in there not everybody has the opportunity to learn python.')
    print('you are really lucky')
print('python is the future! you are on the right track')






    