'''
Requirement:

Build a Number guessing game, in which the user selects a range, for example: 1, 100.
And your program will generate some random number in the range, for example: 42.
And the user needs to guess the number.
If his answer is 50, then you need to tell him. “Try Again! You guessed too high”
If his answer is 20, then you need to tell him. “Try Again! You guessed too low”
When he finally guesses it, you need to tell him, how many times he guesses.

Implementation steps:
1) Define 2 variables -lower / upper, get values from console.
2) Define 1 variables - answer, use random.randint function.
3) Loop, until user answer is the same as guess.number.
'''
import random
guess = 0
x = random.randint(1,100)

while True:
    guess_number = int(input('guess num(int)'))
    if guess_number > x:
        print('bigger than x')
        guess+=1

    if guess_number < x:
        print('smaller to x')
        guess+=1

    if guess_number == x:
        print('you win')
        print(f'you end it with {guess} ')
        break

print('game over')

