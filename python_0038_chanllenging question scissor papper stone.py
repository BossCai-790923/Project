while True:
    a = input('player a scissor,paper,rock,exit, "input first letter!!!" :')
    b = input('player b scissor,paper,rock,exit, "input first letter!!!" :')
    while a != 'e' and b != 'e':
        if a == b:
            print('again!')
            break
        if a == 's' and b == 'r':
            print(f'player a failed with {a} attack {b} , rock cannot be cut')
            break
        if a == 's' and b == 'p':
            print(f'player a win with {a} attack {b} ,yes, that is what scissor do ')
            break
        if a == 'r' and b == 'p':
            print(f'player a failed with {a} attack {b} ,you are killing yourself')
            break
        if a == 'r' and b == 's':
            print(f'player a win with {a} attack {b} , rock is a good thing for attack scissors ')
            break
        if a == 'p' and b == 'r':
            print(f'player a win with {a} attack {b} , paper is a good thing for attack rock ')
            break
        if a == 'p' and b == 's':
            print(f'player a failed with {a} attack {b} , that is a bad choise for paper. ')
            break
        print('turn 1 finished')
        break
        print('if you want to exit , print e')
        want_to_exit_a = input('do you want to exit : if yes, print e ,if no, print n : ')
        want_to_exit_b = input('do you want to exit : if yes, print e ,if no, print n : ')
        if want_to_exit_a == 'e':
            print('player a want to exit')
        elif want_to_exit_a and want_to_exit_b == 'e':
            print('a and b want to exit , game closed')
        else:
            print('player b wants to exit')
        if a != 's' or a != 'r' or a != 'p' or a != 'e' or b != 's' or b != 'r' or b !='p' or b != 'e':
            print('someone print un rec. symbol. game start again')
            break

    else:
        print('shut it down if you dont like it')
        break
