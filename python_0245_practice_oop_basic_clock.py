'''
Requirement:
Use OOP, implement a Clock class
'''

import time

class Clock:

    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __next_second(self):
        self.second += 1

        if self.second == 60:
            self.second = 0
            self.minute += 1

        if self.minute == 60:
            self.minute = 0
            self.hour += 1

        if self.hour == 24:
            self.hour = 0

    def __show_time(self):
        print(f"{self.hour:0>2d}:{self.minute:0>2d}:{self.second:0>2d}")
        '''
        0>2d
        0 : if number (self.hour) is not wide enough, put '0' to make it wide enough
        > : put '0' on the left, put the number on the right
        2 : total width is 2, so if the self.hour is 1, then it becomes 01
                                 if the self.hour is 1, then it becomes 10
        d : the number is of int type
        '''

    def run(self):
        while True:
            self.__show_time()
            self.__next_second()
            time.sleep(1) # Your program will sleep for 1 second

    def __str__(self):
        return f"{self.hour}:{self.minute}:{self.second}"


# MAIN PROGRAM BEGIN ==========================
if __name__ == '__main__':
    clock = Clock(9, 50, 5)
    # clock.__show_time()
    # clock.__next_second()
    # clock.__show_time()
    clock.run()

'''
IMPORTANCE !!! ------------------------------------------------------------------------------------------
After I finish class Clock, somebody else may import it, use it, create a Clock object.
I don't want the expose next_second() / show_time() method
if he calls clock. next_second(), my clock will be inaccurate
Solution:
I add double underscore in front of the 2 methods. They become:
__next_second()
__show_time()
The 2 methods will be hidden from outside, they can only be used within the class Clock
---------------------------------------------------------------------------------------------------------
'''