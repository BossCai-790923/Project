#Every python program we've seen so far is sequenrial execition
#code is executed strictry ine after line, from top to bottom
#flow ctrl can skip over some lines of the code
#if statement
today = input('what day is it today?')
print('i get up at 7am')
print('i have my breakfast at 8am')
#IMPORTANCE!!!/////////////////////////////
#if <boolean expression>:
#   < statement >
#   < statement >
#   < statement >
#1> if<~~> ends with a ':'
#2> all code under 'if' section are indented 4 spaces
#3>treat the 3 print statements as a 'block' , because they are indented 4spaces.
#    The 'block' will be executed if today == 'Sunday' is True, otherwise ,the'block' won't get executed
#//////////////////////////////////////////
if today == "sunday":#sunday is a boolean expression.
    print('I attended mr Fan`s Python lesson at 9 am.')
    print('I start working on my homeworks at 10.30am')
    print('home work is done at 11:30 am')
print('I have mu lunch at 12.pm')
print('i play football with friends at 5 pm.')
print('i have my dinner at 7pm')
print('i g to bedat 10pm')