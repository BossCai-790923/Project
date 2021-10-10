

'''
Requirement:
Print out how many students objects are created in total.

Analysis:
we need to define a variable to save this info - students_count

'''


class Student:


    student_count = 0

    # IMPORTANCE!!! -----------------------------------------
    # class variables are defined directly under class
    #
    # all class instances share the same class variables
    # variable student_count belongs to the class Student.
    # It doesn't belong to any concrete Student object / instance. So you can't use self pointer to use class variables.
    # -------------------------------------------------------


    def __init__(self, name, score):
        self.name = name
        self.score = score

        Student.student_count += 1
        # You can only use 'Classname.' to use the class variable


    def say_his_score_loudly(self):
        print(f"Good morning Sir! My name: {self.name}! my score is: {self.score}")


    @classmethod
    def print_student_total_count(cls):
        print(f"Total students: {cls.student_count}")

    # 1) class method's 1st parameter is 'cls'
    # 2) cls is a pointer which points to the class object
    # 3) Revise: self is a pointer which points to the instance object.
    # 4) Add annotation '@classmethod'



sandy = Student('Sandy', 57)
susan = Student('Susan', 97)

sandy.say_his_score_loudly()
susan.say_his_score_loudly()


# There are 3 ways to use a class variable

# Solution 1) use Classname.
print(Student.student_count)

# Solution 2) use instance - because class variables are shared by all Class instances.
print(sandy.student_count)

# Solution 3) use__class__
print(sandy.__class__.student_count)

# IMPORTANCE!!! ------------------------------------
# In python, everything is a object.
# sandy and susan : instance object.
# Student         : class object.
# sandy.__class__ : class object. Get the 'class object' from an 'instance object'
#                   sandy.__class__ = Student
# --------------------------------------------------

# Solution 1) use Classname.
Student.print_student_total_count()

# Solution 2) use instance - because class variables are shared by all Class instances.
sandy.print_student_total_count()

# Solution 3) use__class__
sandy.__class__.print_student_total_count()

