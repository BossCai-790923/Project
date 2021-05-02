'''
important !!!!!!!!!!!!!!!!!!!!
import the random module into your python file.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''
import random

#important_____________________________________________________________________________
# random.randint (1,10) is composed of 4 parts
#
#1) random          :module name
#2) .               : separate module name and the function name.
#3) randint         :randint is a function
#                    it is under the random module
#                    it will return a random number in range[1,10]
#4) (1,10)          :both 1 and 10 are parameters.
#                                      ^it is some value you pass to a function.
#important_____________________________________________________________________________

#util method / util class -工具类
################################################################################
# i = 0
# while i <100:
#     random_int = random.randint(1,100)
#     print(random_int)
#     i += 1
# ##############################################################
# i = 0
# while i < 100:
#     random_number = random.random() # random float in range [0,1)
#     print(random_number)
#     i += 1
##############################################
i = 0
while 1 < 100:
    random_number = random.uniform(1.2 , 7.8)
    print(random_number)
    i += 1