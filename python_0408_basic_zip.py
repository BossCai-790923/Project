'''
python zip works just like the physical zipper on a bag.
Interlocking pairs of teeth on both sides of the zipper are pulled together to close an opening.
It is named after physical zipper.
'''

print("Example1: zip 2 lists ----------------------------")

numbers = [1,2,3]
letters = ['a', 'b', 'c']

zip_1 = zip(numbers, letters)
print(zip_1)

# Python zip() function returns an iterator, which generates a series of tuples.
# Use list() to convert a zip to a list
list_1 = list(zip_1)
print(list_1)

print("Example2: zip 2 sets ----------------------------")
s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}

zip_2 = zip(s1, s2) # why it is not [(2, 'b'), (3, 'a'), (1, 'c')]? Because set is UNORDERED!


list_2 = [*zip_2]
print(list_2)

print("Example3: zip 3 lists ----------------------------")
integers = [1, 2, 3]
lettters = ['a', 'b', 'c']
floats = [4.0, 5.0, 6.0]
zip_3 = zip(integers, lettters, floats)
list_3 = [*zip_3]
print(list_3)


print("Example4: zip 2 ranges which are of different length ----------------------------")

list_4 = list(zip(range(5), range(100)))
print(list_4)

'''
Since 1st range() length is 5, so zip() output a list of 5 tuples. The remaining 95 elements from the 2nd range() is ignored.
'''

print("Example5: 2 star unpacking -----------------------------")
list_5 = [(1,2,3), (4,5,6)]
print(list_5)

list_5_transposed = [*zip(*list_5)]
print(list_5_transposed)