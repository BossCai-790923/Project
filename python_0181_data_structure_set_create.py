def using_curly_braces():
    set1={1,2,3,4,5}
    print('set1=',set1)
    print('-------------------------------------------')
    
    
    dict1={}
    print('{}_is_a_',type(dict1))
    print('-------------------------------------------')

def using_set_constructor_from_list_tuple_range_str():
    #create an emptty seet
    set2=set()
    print('set2=',set2)
    print('________________________________')


    a_list=[1,1,2,2,3,3]
    set3=set(a_list)
    print('set3 =',set3)
    print('________________________________')
    set4=set([1,1,2,2])#NO
    print('set4 =',set4)
    print('________________________________')

    set5 = set((1,1,2,2))
    print('set5 =', set5)
    print('________________________________')

    range1= range(1,10)
    set6=set(range1)
    print('set6 =', set6)
    print('________________________________')

    set7 = set('Hello,python!')
    print('set7 =', set7)
    print('________________________________')

#######################################
#set is unordered
#duplicate value are only kept once:there is only one 'l'and one 'o'
#######################################
def using_set_constructor_from_dict():
    dict1={1:'a',2:'b',3:'c'}
    set8=set(dict1)
    print(f'set(dict1) gives you a set with dict2"s keys:{set8}')

    set9=set(dict1.values())
    print(f'set(dict1.values) gives you a set with dict2"s keys:{set9}')

    set10=set(dict1.items())
    print(f'set(dict1.items) gives you a set with dict2"s keys:{set10}')



using_curly_braces()
using_set_constructor_from_list_tuple_range_str()
using_set_constructor_from_dict()

# IMPORTANCE !!! -----------------------------------
#
# You can put an 'iterable' object into the set constructor -> set()
# What is an 'iterable' object?
# list  is iterable     because     for e in a_list:
# tuple is iterable     because     for e in a_tuple:
# range is iterable     because     for i in range(10):
# str   is iterable     because     for ch in "hello":
# dict  is iterable     because     for key in a_dict:
#                                   for value in a_dict.values():
#                                   for key, value in a_dict.items():
#
# What is an 'iterable' object?
# An iterable object is capable of returning its members one by one.
# An iterable object is anything that you can loop over with a for loop.
# ---------------------------------------------------



# HOMEWORK ------------------------------------------
# Create another 5 set from your daily life using all kinds of data / method
# Put int / float / bool / tuple
# Use set()
# ---------------------------------------------------
def AbC():
    vabc=set('qpowfiouqwiureriueqtyoendshfflahgljsdlnabdazzvxczvbnmbcxvxz')
    print(vabc)
AbC()

def vowel():
    vowel=set(list('aeioueeiouioueaoiueaouaioeuaeoiuaoieiuaeouaoiueoauoieuaoiueoiauoia'))
    print(vowel)
vowel()

def number():
    num=set(tuple('13032131054604879079874651230003154679846499555612313200235645646489879841231230'))
    print(num)
number()

def marks():
    mk=set('~!@#$%^&*()_+}{|":<>?/,.;[]\=-!@#$%^&*()_)(*&^%$#@#$%^&%$#@!~~``~~!@#$%$#@#$%^&*())(**+-={}}}{][\];''.,//*-++-*/')
    print(mk)
marks()