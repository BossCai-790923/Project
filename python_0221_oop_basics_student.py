'''
Now we learn:
-------------------------------------
Object-Oriented Programming
-------------------------------------
'''


# CLASS DEFINITION BEGIN ----------------------------------------------------------------

class Student:

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.school = 'NUS'


    def say_his_score_loudly(self):
        print(f"Good morning Sir! My name: {self.name}! I come from {self.school}, my score is: {self.score}")

    def go_to_school(self):
        pass

    def play_game(self):
        pass

'''
Q) What is class?
A) Class is like a template. From template, you can copy a lot of objects.
   Class is like a factory. From a factory, you can produce a lot of products.
   From class, you can create many objects, hundreds / thousands / millions objects.
   
   Class defines what a object looks like -- using attributes.
   Class defines what a object can do -- using methods.
   
   
Q) How to define a class?
A) class     :  You start with keyword 'class' when you define a class.
                Just like you start with keyword 'def' when you define a function.
   Student   :  class name. Letter S in uppercase
   
Q) What is magic method __init__ ?
A) Python will automatically invoke this magic method __init__
   whenever you try to instantiate a Student instance, or we say
   whenever you try to create      a Student object, or we say
   whenever you call the Student constructor
    
   In summary, the magic method __init__ is Student constructor.
   In summary, when we call Student('Sandy', 57), it will call the magic method __init__(self, name, score)
   You don't need to pass in 'self', you just need to pass in name & score
   Python will add 'self' for you.
   
   'instantiate' means 'create', means 'calling the constructor'
   'instance'    means 'object', means 'a copy of the template(class means template)', means a product of the factory(class means factory)
  
   
Q) What is the 1st parameter self in the magic method __init__? 
A) it means 1) the current object
            2) the product you are producing right now. 
            
   self is a pointer, it points to the current object
   self.name means the current student's name 
   self.score means the current student's score
   
   All methods inside class have their 1st parameter -> self, so that you can use self.name / self.score in any methods of the class Student.
   
Q) What is attribute 'name' & 'score'? 
A) You define attributes in the magic method __init__
   All student objects / instances have name and score attributes.
   
   Similarly, you can define as many as attributes as you like, for example: 
   self.age = age
   self.gender = gender
   self.class = class
   
   self.age  :  the age attribute of the current student object.
                self.age can be used in any methods of class Student, as all methods use 'self' as their 1st parameter. 
                
   age       :  the parameter of the magic method __init__
                age is only valid inside the magic method __init__
'''




# PREPARE DATA BEGIN --------------------------------------------------------------------
student_1 = Student('Sandy', 57) # ignore 'self' parameter
student_2 = Student('Susan', 97)

'''
Student is a class
'student_1' is a Student object / instance
'student_2' is another Student object / instance
You create the 2 student objects by calling Student class constructor
'''



# MAIN PROGRAM BEGIN --------------------------------------------------------------------
if __name__ == '__main__':

    # Usage 1) I can invoke student objects' method
    student_1.say_his_score_loudly() # you can ignore the 'self' parameter
    student_2.say_his_score_loudly()

    # Usage 2) I can access student objects' attributes directly
    print(f'Student_1 info: {student_1.name} from {student_1.school}, with score {student_1.score}')

    # Usage 3) I can assign new values to student objects' attributes directly
    student_1.name = 'Billy'
    student_1.score = 88
    student_1.school = 'NTU'

    student_1.say_his_score_loudly()



'''
---------------------------------------
What is class - further explanation
---------------------------------------
Class is a definition of something from our real life. It is a noun. 
Class is a blueprint.
Class includes attributes and behaviors (methods) 
As long as it is noun, then you can define it as a Class. Dog / Building / Computer / Car
'''