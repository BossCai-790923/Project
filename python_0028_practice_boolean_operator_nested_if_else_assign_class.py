# we have some studens base on their math/science/english score,we'll assign them to the following classes
# elite class - all 3 subjects should have score higher than 85
#math elite class - math score higher than 85 and 3 subjects average higher than 75 and no subject lower than 70
# science elite class -science score higher than 85 and 3 subjects average higher than 75 and no subject lower than 70
# english elite class -english score higher than 85 and 3 subjects average higher than 75 and no subject lower than 70
#experss class average score higher than 75 and no subjects  lower than 65
#normal class - other students
class_name = ' '
#sp 0
math_score = float(input('math score :'))
science_score = float(input('science score:'))
english_score = float(input('english score:'))
#sp 1  calc average score
average_score  = (math_score + science_score + english_score) / 3
print(f' your average score is {average_score:.2f}')
#sp2 check for elite
if math_score > 85 and science_score>85 and english_score>85:
    class_name = 'Elite class'
#Imp___________________________________________________
#nested if elif else - you can put 'if elif else' under if(elif,else) clause
#-_____________________________________________________
#sp 3 check math(eng,sci) elite class
elif (math_score > 85 or science_score > 85 or english_score > 85)and average_score > 75  and math_score>= 70 and science_score>= 70 and science_score>=70 and english_score>=70:
    if math_score > 85:
        class_name = 'math elite class'
    elif science_score > 85:
        class_name = 'science elite class'
    else:
        class_name = 'english elite class'

#sp 4
elif average_score > 75 and math_score >= 65 and english_score>=65 and science_score>= 65:
    class_name = 'Experss class'

#sp 5
else:
    class_name = 'Nor mal class'
print(f'you are assigned to {class_name}')
