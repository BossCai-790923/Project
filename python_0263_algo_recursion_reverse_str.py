
def reverse_str(str1):
    reversed_str=''

    # base case:
    if len(str1) == 1:
        return str1


    else:
        for i in range(1,len(str1)+1):
            reversed_str+=reverse_str(str1[-i])
        return reversed_str




reversed_str = reverse_str('Hello!')
print(reversed_str)