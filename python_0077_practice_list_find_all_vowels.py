'''
Requirement:
User will supply a word from console.
Requirement 1) You need to find all the vowels(a/e/i/o/u) in the word.
Requirement 2) Further enhance your code, only collect vowels once (we don't want duplicate vowels)
'''
vow=list('aeiou')
word=input('search vowels:')
find=[]
for letter in word:
    if letter in vow or vow in find:
        print(vow,end=' ')
print('\n')
print(find)
real=[]
# list1 = [1, 2, 3, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9]
# real += list(set(find))
# print(real)
for i in find:
    if not i in real:
        real.append(i)
print(real)