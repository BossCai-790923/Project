import sys

def readline_example():
    print("Name: ", end='')
    name = sys.stdin.readline().rstrip()
    print(f"Hello, {name}!")


def input_example():
    name = input("Name: ")
    print(f"Hello, {name}!")


# readline_example()
input_example()

# input() vs sys.stdin().readline()
# Both read the whole line which you input.

# Difference:
# input()                : The line does not end with '\n'
# sys.stdin.readline()   : The line ends with '\n'
