def describe_pet(type,name):
    print('I have a',type)
    print(f'my {type}s name is {name}')

describe_pet(type='hamster',name='Harry')
#this is called keyword arguments.
#you explicitly tell python whichu argument si mapped to which parameter.

describe_pet(name='Billy',type='dog')
