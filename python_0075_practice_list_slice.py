a = list('abcdefgh')

print(a[:]) #all ['a','b','c',...'h']
print(a[:5]) #0-4['a'...'e']
print(a[:-1]) #0-last2['a',...,'g']
print(a[4:]) #4-last['e', ..., 'h']
print(a[-3:]) #-3-last['f',...'h']
print(a[2:5]) #2-4['c',...,'e]
print(a[2:-1]) #2-last2['c',...,'g']
print(a[-3:-1]) #last3-last2['f','g']