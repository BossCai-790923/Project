# CLASS DEFINITION BEGIN =============================

class Car:
    '''
    A simple attempt to represent a car.
    '''

    def __init__(self, color, brand, model, power):
        self.power = power
        self.model = model
        self.brand = brand
        self.color = color

    def start(self):
        print(f"The car starts slowly")

    def speed_up(self, top_speed):
        print(f"The car speeds up, and maintains at speed {top_speed} mph.")

    def go_to(self, destination):
        print(f"The car is on its way to {destination}.")

    def __str__(self):
        # return 'This is just a car'
        return f"This is a {self.color} color, {self.brand} {self.model} car. It is powered by {self.power}"

    # IMPORTANCE !!! -----------------------------------------------------
    # magic method __str__
    # it helps customize the content you see when you print the object.
    # Please implment it as well when you define a class
    # --------------------------------------------------------------------


# PREPARE DATA BEGIN ==================================
car1 = Car('green', 'Ford', 'Mustang', 'gasoline')
car2 = Car('red', 'Toyota', 'Prius', 'electricity')
car3 = Car('blue', 'Volkswagon', 'Golf', 'diesel')

car_list = [car1, car2, car3]

# MAIN PROGRAM BEGIN ================================

if __name__ == '__main__':

    car1.start()
    car1.speed_up(80)
    car1.go_to('Sentosa')

    for car in car_list:
        print(car)
        # print(id(car))

    print(f'hecadecimal 0x00000127F2920FA0 to decimal is: ', int('0x00000127F2920FA0', 16)) # 1271085010848
