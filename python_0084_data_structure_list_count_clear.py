fruits=['Apple', 'Orange', 'Banana', 'Pear'] * 2

fruits.remove('Orange')
fruits.append('Apple')#['Apple', 'Banana', 'Pear', 'Apple', 'Orange', 'Banana', 'Pear', 'Apple']

print(fruits)
#-fruits.count('orange')
print('there are ',fruits.count('Orange'),'Orange in fruits')
print('there are ',fruits.count('Apple'),'Apple in fruits')
print('there are ',fruits.count('Banana'),'Banana in fruits')
#fruits.clear()
fruits.clear()
print(fruits)