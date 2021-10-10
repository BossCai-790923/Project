import turtle
from turtle import *
import random
t=turtle.Pen()
t.speed(0)
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']


bgcolor('black')

for x in range(360):

    t.pencolor(colors[random.randint(0,5)])
    t.begin_fill()
    t.width(x // 100 + 1)
    t.forward(x)
    t.left(59)
    t.pencolor(colors[random.randint(0,5)])
    t.begin_fill()
    t.width(x // 100 + 1)
    t.forward(x)
    t.left(59)
    t.end_fill()