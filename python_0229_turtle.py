import turtle
from turtle import *
t=turtle.Pen()
t.speed(0)
# -square ---------------------------

t.pencolor('green')
for i in range(4):
    t.forward(50) # draw straight line 50 unit
    t.right(90) # turn right 90 degree

# -star -------------------------------
t.penup()
t.goto(100, 100)
t.pendown()

t.pencolor('red')
for i in range(5):
    t.forward(100)
    t.right(144)

# -circle 1 ---------------------------
t.penup()
t.goto(-100, 100)
t.pendown()

t.pencolor('blue')
for i in range(360 // 10): # 10 degree * 36 = 360 degree
    t.forward(10)
    t.right(10)



# -circle 2 -------------------------
t.penup()
t.goto(0, 100)
t.pendown()

t.pencolor('yellow')
t.circle(100)


# -flower ----------------------------
t.penup()
t.goto(-100, -100)
t.pendown()

t.pencolor('black')
for i in range(100):
    t.forward(100)
    t.left(123)


done()