#requirement: base on user input age,tell the current user is a adult,a teenager, a kid or a baby.

age=int(input('How old are you???:'))
#IMPORTANCE!!!---------------------------------------------
#if elif else gives you multiple choices.
# U can pick one path
#----------------------------------------------------------
if age >= 20:
    print('you are a adult now.')
    print('you can start a software programmer career')
elif age >= 13:#</> else if
    print('you are still a teenager.')
    print('you should start taking some python lesson')
elif age > 3 :
    print('you are still a kid!')
    print('play time at your age. enjoy!')
else:
    print('you are still a baby.')
    print("eating,drinking,sleeping,P**ping,crying......")