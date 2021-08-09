'''
__name__ variable is a special python variable: python reserved variable
there are Double UNDERscore in the front and end.
such variable has a special name in Python - dunder variable
here is what happens:
as soon as your python program starts, either you run it directly, or it is imported indirectly
python will assign a value to variable __name__, its value depends on how your python program is used
if you run it directly:  __name__ = '__main__'
if it is imported:       __name__ = file name
'''


def hello(name):
    print("Hello", name)



if __name__ == '__main__':
    hello("XXX")
    print(f"variable '__name__' has value {__name__}")