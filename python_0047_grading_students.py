'''
Requirement:
Step 1) Get student count from console. Ask user to tell you how many students in total.
Step 2) For each student, let user to input the student score.
Step 3) If the difference between the score and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
        If the score is less than 58, no rounding occurs, as it is a failing score.
        For example: score = 84, round to 85 (because 85 - 84 less than 3)
                     score = 57, no rouding (because 57 is less than 58)
                     score = 67, no rounding ( because 70 - 67 is 3 or greater)
Step 4) Print the final score for the student
'''

how_many_students = int(input('howmany: '))

for student_none in range (how_many_students):
    student_score = int(input('score: '))
    if student_score % 5 >= 3 and student_score >= 57:
        student_score += (5-student_score % 5)

    print(student_score)