import turtle
from turtle import *
t=turtle.Pen()
t.speed(0)
def square(length):
    for i in range(4):
        t.forward(length)
        t.right(90)

for i in range(365 // 5):
    square(100)
    t.right(5)

done()