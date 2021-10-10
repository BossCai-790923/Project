'''
integer can be in different base.

Base 10 -> decimal              1   2   3   4   5   6       7       8       9       10      11      12      13  ... 15 16
Base 2  -> binary               1   10  11  100 101 110     111     1000    1001    1010    1011    1100    1101    1110    1111
Base 8  -> octal                1   1   3   4   5   6       7       10      11      12      13      14      15
Base 16 -> hecadecimal          1   1   3   4   5   6       7       8       9       a       b       c       d   ... f  10

'''

def convert_decimal_to_binary_octal_hecadecimal():
    print(bin(10)) # 0b1010
    print(oct(10)) # 0o12
    print(hex(10)) # 0xa
    print(hex(100000000000000001)) # 0x16345785d8a0001


convert_decimal_to_binary_octal_hecadecimal()


def convert_binary_octal_hecadecimal_to_decimal():
    print('binary 1010 to decimal is:', int("1010", 2))
    print('octal 12 to decimal is:', int("12", 8))
    print('hecadecimal a to decimal is:', int("a", 16))

    print('binary 1010 to decimal is:', int("0b1010", 2))
    print('octal 12 to decimal is:', int("0o12", 8))
    print('hecadecimal a to decimal is:', int("0xa", 16))


convert_binary_octal_hecadecimal_to_decimal()