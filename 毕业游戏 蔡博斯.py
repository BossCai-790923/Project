import turtle
import time
import random
l = turtle.Pen()
we = []
wexy = [0,0,0,0,0]
en = []
enxy = [800,800,800,800,800]
x = [0,0,0,0,0]
win = 0
attack = True
l.speed(0)
#print line
for i in range(7):
    l.up()
    l.goto(-500,300-100*i)
    l.down()
    l.fd(1000)
l.up()
l.ht()
for i in range(5):
    t = turtle.Pen()
    t.color('red')
    t.shape('turtle')
    t.up()
    t.speed(0)
    t.goto(-400+200*i,400)
    t.down()
    t.rt(90)
    t.speed(3)
    en.append(t)
    
for i in range(5):
    t = turtle.Pen()
    t.color('blue')
    t.shape('circle')
    t.up()
    t.speed(0)
    t.goto(-400+200*i,-400)
    t.down()
    t.lt(90)
    t.speed(3)
    we.append(t)


wk_msg = '''
********************************
* Welcome to my GAME!          *
*                    -boss cai *
********************************
________________________________
you are going to sure blue and
red are with 1 mile and all ship
will shoot.
if one of the ship is hit by
monster,game ends.
'''
print(wk_msg)
while attack:
    for i in range (5):
        x[i] =int(input('go ship as 0/1 , and when you enter one, press "enter" : '))
    for i in range (5):
        if x[i] == 1:
            we[i].fd(100)
            wexy[i]+=100
    for i in range(5):
        if  enxy[i] - wexy[i] == 100 :
            win += 1
    if win == 5:
        l.up()
        l.goto(0,0)
        l.down()
        l.color('red')
        l.down()
        l.write('WIN',font=("Arial", 30), align="center")
        break
    for i in range(5):
        x = random.randint(0, 1)
        if x == 1:
            en[i].fd(100)
            enxy[i] -= 100
    for i in range(5):
        if wexy[i]==enxy[i]:
            l.up()
            l.goto(0,0)
            l.color('blue')
            l.down()
            l.write('LOOSE',font=("Comic Sans MS", 50), align="center")
            attack = False
            break
    x=[0,0,0,0,0]
    win = 0
time.sleep(20)




turtle.mainloop()
    
