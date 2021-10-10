
# CLASS DEFINITION BEGIN =====================================

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.tricks = []


    def sit(self):
        if 'sit' in self.tricks:
            print(f"{self.name} is now sitting")
        else:
            print(f"{self.name} doesn't know how to sit.")


    def roll_over(self):
        if 'roll over' in self.tricks:
            print(f"{self.name} rolled over!")
        else:
            print(f"{self.name} doesn't know how to roll over.")


    def learn_trick(self, trick_name):
        self.tricks.append(trick_name)
        print(f"{self.name} has learnt new trick: {trick_name}")


# PREPARE DATA BEGIN =========================================

my_dog = Dog('Willie', 6) # Calling Dog constructor to instantiate a dog instance; or to say, to create a dog object. Calling the magic method __init__
your_dog = Dog('Lucy', 3)

# MAIN PROGRAM BEGIN =========================================

if __name__ == '__main__':

    my_dog.sit()
    my_dog.roll_over()

    my_dog.learn_trick('sit')
    my_dog.learn_trick('roll over')

    my_dog.sit()
    my_dog.roll_over()

    print(f"My dog's name is {my_dog.name}")
    print(f"My dog is {my_dog.age} years old.")

    '''
    When you are inside the class Dog -> self.name / self.age
    When you are outside the class Dog -> my_dog.name / my_dog.age
    '''

    print(my_dog) # <__main__.Dog object at 0x000002715CF48FD0>
