
def is_palindrome(str1):

    # base case 1
    if len(str1) == 1:
        return True

    # base case 2
    if str1[0] != str1[len(str1) - 1]:
        return False

    if str1[0] == str1[len(str1) - 1]:
        return True

print(f"'TENET' is {is_palindrome('TENET')}")
print(f"'abcdcba' is {is_palindrome('abcdcba')}")
print(f"'hello' is {is_palindrome('hello')}")