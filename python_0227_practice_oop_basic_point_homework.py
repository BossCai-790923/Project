from math import sqrt

# CLASS DEFINITION BEGIN ==========================

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(f"New point({x},{y}) is created.")

    def move_to(self, x, y):
        print(f"Moving point({self.x},{self.y}) to new location ({x},{y})")
        self.x = x
        self.y = y


    def move_by(self, delta_x, delta_y):
        print(f"Moving point({self.x},{self.y}) by {delta_x} and {delta_y}")
        self.x += delta_x
        self.y += delta_y

    '''
    dx -> delta x
    In math, delta means 'increased by'
    '''

    def distance_to(self, other):
        a = self.x - other.x
        b = self.y - other.y
        return sqrt(a ** 2 + b ** 2)


    def __str__(self):
        return f'({self.x},{self.y})'

    def to_tuple(self):
        '''
        Create a tuple from x and y
        '''
        return self.x, self.y

    def create_new_point(self, delta_x, delta_y):
        new_x = self.x + delta_x
        new_y = self.y + delta_y
        return Point(new_x, new_y)


# MAIN PROGRAM BEGIN =================================

if __name__ == '__main__':

    print("Creating p1 -------------------------")
    p1 = Point(-10, -10)

    print("Moving p1 to -------------------------")
    p1.move_to(3, 5)

    print("p1 location -------------------------")
    print(f"p1 location: {p1}")

    print("Creating p2 -------------------------")
    p2 = Point(0, 0)

    print("Moving p2 by-------------------------")
    p2.move_by(-1, 2)

    print("p2 location -------------------------")
    print(f"p2 location: {p2}")

    print("Calculating p1 to p2 distance ------")
    print(p1.distance_to(p2))