'''
python - dict
java - hashmap / hashtable
c++ _ unordered_map
extremely efficient at looking up a value
'''
import random
import time

list1 = list(range(1000000))

# shuffle the list
random.shuffle(list1)

time_start = time.time()
for i in range(100):
    print(i, 'is at index: ', list1.index(i))
time_end = time.time()
print('time cost', time_end - time_start, 'seconds')

print('---------------------------------------------------------')

dict1 = {}
for i in range(1000000):
    dict1[i] = i

time_start = time.time()
for i in range(100):
    print(i, 'is found in dict: ', dict1[i])
time_end = time.time()
print('time cost', time_end - time_start, 'seconds')

'''
1) load factor = 0.75
   Initially, the bucket size is 16

   16 * 0.75 = 12
   When you've put 12 entries(key/value pair), the dict / hashmap will resize to 32 buckets

2) hash algo is very important!

''''''
python - dict
java - hashmap / hashtable
c++ _ unordered_map
extremely efficient at looking up a value
'''
import random
import time

list1 = list(range(1000000))

# shuffle the list
random.shuffle(list1)

time_start = time.time()
for i in range(100):
    print(i, 'is at index: ', list1.index(i))
time_end = time.time()
print('time cost', time_end - time_start, 'seconds')


print('---------------------------------------------------------')

dict1 = {}
for i in range(1000000):
    dict1[i] = i

time_start = time.time()
for i in range(100):
    print(i, 'is found in dict: ', dict1[i])
time_end = time.time()
print('time cost', time_end - time_start, 'seconds')


'''
1) load factor = 0.75
   Initially, the bucket size is 16
   
   16 * 0.75 = 12
   When you've put 12 entries(key/value pair), the dict / hashmap will resize to 32 buckets
   
2) hash algo is very important!
   
'''