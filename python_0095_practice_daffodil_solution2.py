for i in range(100, 1000):
    i_str = str(i)
    '''
    i              is   int 123
    i_str          is   str '123'
    i_str[0]       is   str '1'      
    int(i_str[0])  is   int 1
    '''
    a = int(i_str[0])
    b = int(i_str[1])
    c = int(i_str[2])
    if a ** 3 + b ** 3 + c ** 3 == i:
        print(i)
