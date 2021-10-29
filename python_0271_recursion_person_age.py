'''
Question:
5 person sit together.
Asking No.5, 'how old are you?', answer: 2yrs older than No.4
Asking No.4, 'how old are you?', answer: 2yrs older than No.3
Asking No.3, 'how old are you?', answer: 2yrs older than No.2
Asking No.2, 'how old are you?', answer: 2yrs older than No.1
Asking No.1, 'how old are you?', answer: 10 yrs.
Use recursive algorithm to implement it.
'''


def age(person_no):


    if person_no==1:
        return 10


    else:
        return 2+age(person_no-1)


print(age(5)) # 18
