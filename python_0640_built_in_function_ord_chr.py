import string


def compare_str():
    print("a > c : ", 'a' > 'c')
    print("apple > cat : ", 'apple' > 'cat')
    print("a > A : ", 'a' > 'A')
    print("z > A : ", 'z' > 'A')
    print('--------------------------------')

compare_str()

'''
unicode -> unified code
'''

def ord_example1():
    print('a', ord('a'))
    print('c', ord('c'))
    print('z', ord('z'))
    print('A', ord('A'))
    print("-------------------------------------")

ord_example1()


def to_binary_example():
    for ch in 'Apple':
        unicode_value = ord(ch)
        bin_value = bin(unicode_value)
        print(ch, 'unicode value is:', unicode_value, 'binary value is: ', bin_value)
    print('---------------------------------------')

to_binary_example()


def ord_example2():
    print(string.ascii_lowercase)
    for i in string.ascii_lowercase:
        print(i, ord(i), sep=" - ", end=', ')

    print('\n---------------------------------')

    print(string.ascii_letters)
    for i in string.ascii_letters:
        print(i, ord(i), sep=" - ", end=', ')
    print('\n---------------------------------')

    print(string.digits)
    for i in string.digits:
        print(i, ord(i), sep=" - ", end=', ')
    print('\n---------------------------------')


ord_example2()

def chr_example():
    print(chr(0x03B5))
    print(chr(0x1F9E1))
    print(chr(0x1F4A6))
    print(chr(0x2663))
    print(chr(0x1F601))
    print(chr(0x1F618))

chr_example()