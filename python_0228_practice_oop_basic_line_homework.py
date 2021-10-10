from python_0227_practice_oop_basic_point_homework import *
import turtle

from turtle import *



# CLASS DEFINITION BEGIN ==========================

class Line:
    def __init__(self, point_a, point_b, color):
        self.point_a = point_a
        self.point_b = point_b
        self.color = color

    def length(self):
        return f"{self.point_a.distance_to(self.point_b)}"

    def draw(self):
        penup()
        color(self.color)
        goto(self.point_a.to_tuple())
        pendown()
        goto(self.point_b.to_tuple())

    def create_parallel_line(self, delta_x, delta_y):
        new_point_a = self.point_a.create_new_point(delta_x, delta_y)
        new_point_b = self.point_b.create_new_point(delta_x, delta_y)
        return Line(new_point_a, new_point_b, self.color)



# PREPARE DATA BEGIN =================================

p1 = Point(30, 50)
p2 = Point(-10, 20)
p3 = Point(50, 20)
line1 = Line(p1, p2, 'green')
line2 = Line(p2, p3, 'red')
line3 = Line(p1, p3, 'yellow')



# MAIN PROGRAM BEGIN =================================

if __name__ == '__main__':
    print(f'line1 length: {line1.length()}')
    print(f'line2 length: {line2.length()}')
    print(f'line3 length: {line3.length()}')

    line1.draw()
    line2.draw()
    line3.draw()

    line3_parallel = line3.create_parallel_line(10, 10)
    line3_parallel.draw()

    hideturtle()
    turtle.exitonclick()