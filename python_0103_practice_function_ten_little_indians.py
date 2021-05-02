'One little, two little, three little Indians   '
'Four little, five little, six little Indians   '
'Seven little, eight little, nine little Indians'
'Ten little Indian boys.                        '
'Ten little, nine little, eight little Indians  '
'Seven little, six little, five little Indians '
'Four little, three little, two little Indians  '
'One little Indian boy.'
n=['One',
    'Two',
    'Three',
    'Four',
    'Five',
    'Six',
    'Seven',
    'Eight',
    'Nine',
    'Ten']
def little_Indians01(int,int1):
    """
    tp indians

    """
    if int == int1 - 1:
        print(n[int-1],'little',n[int+1-1],'little',n[int+2-1],'little Indians')
    if int==int1+1:
        print(n[int-1],'little',n[int-1-1],'little',n[int-2-1],'little Indians')
def little_Indians02(int):
    """
    tp indians

    """
    if int==1:
        print(n[int-1],'little Indian Boy')
    else:
        print(n[int-1],'little Indian Boy')
little_Indians01(1,2)
little_Indians01(4,5)
little_Indians01(7,8)
little_Indians02(10)
little_Indians01(10,9)
little_Indians01(7,6)
little_Indians01(4,3)
little_Indians02(1)
