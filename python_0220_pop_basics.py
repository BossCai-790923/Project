'''
--------------------------------------------
procedure oriented programming - pop
--------------------------------------------
All we learnt so far, they are all procedure-oriented programming
what we did in our program?
1)we define some variable (int/float/bool/list/set/tuple/ dict)
2)we define some function (do_this()/do_that()/calculate_a_value(param)/populate_a_dict())
3)our main program begins (use variables & functions defined previously)
'''


# prepare data begin -------------------------------
student_1 = {'name': 'michael', 'score': 95}
student_2 = {'name': 'bob', 'score': 81}

# function definition begin ------------------------
def say_score(student):
    print(f"Good morning Sir! my name: {student['name']}! my score is: {student['score']}")

# main program begin -------------------------------
say_score(student_1)
say_score(student_2)