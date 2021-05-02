#user an pass or not pass parameter border
#defult varable should be put in last.

def banner(message,border='-'):
    '''
    this function create a border
    '''
    line=border*len(message)
    print(line)
    print(message)
    print(line)
banner('singapore is a beautiful city')
banner('happy sunday!','*')
'''
requirement
def a function greeeeeeeeeeeeeeeeeeeeet friends! 
'''
def greeeeeeeeeet(name,defult='good morning'):
    greet=name+','+defult
    print(greet)
greeeeeeeeeet('Tom','hello')
greeeeeeeeeet('Tom')
