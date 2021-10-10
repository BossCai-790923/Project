'''
The following values are treated as False:
empty list / empty tuple / empty dict / empty str / 0
The following values are treated as True:
non-empty list / non-empty tuple / non-empty dict / non-empty str / non 0
'''


empty_list = list()
empty_tuple = tuple()
empty_dict = dict()
empty_str = ''
int_0 = 0

non_empty_list = ['hello']
non_empty_tuple = ('python',)
non_empty_dict = {'hello':'python'}
non_empty_str = 'hello python'
non_int_0 = -1

def full_or_not(*value_tuple):
    for i in value_tuple:
        if i :
            print(i,'is full')
        else:
            print(i,"isn't full")
    print('-*'*25)

if __name__ == '__main__':
    full_or_not(empty_list, empty_tuple, empty_dict, empty_str, int_0)
    full_or_not(non_empty_list, non_empty_tuple, non_empty_dict, non_empty_str, non_int_0)