import time


def sleep_example():
    print("Now")
    time.sleep(2.4) # program pauses 2.4 seconds
    print("2.4 seconds later")

def localtime_example():
    current_time = time.localtime()
    print(current_time)
    print(type(current_time))

    print("Year:",   current_time[0], current_time.tm_year)
    print("Month:",   current_time[1], current_time.tm_mon)
    print("day:",   current_time[2], current_time.tm_mday)
    print("hour:",   current_time[3], current_time.tm_hour)
    # print("Year:",   current_time[0], current_time.tm_year) # homework: type all these attributes
    # print("Year:",   current_time[0], current_time.tm_year)
    # print("Year:",   current_time[0], current_time.tm_year)
    # print("Year:",   current_time[0], current_time.tm_year)
    # print("Year:",   current_time[0], current_time.tm_year)
    # print("Year:",   current_time[0], current_time.tm_year)

# iMPORTaNce !!! ------------------------------------
# time.localtime() gives you a object of class struct_time, which is a sub class of base class Tuple
# So firstly, struct_time object is a tuple
# Secondly, as a object of struct_time class, we can also access its attributes (properties)
# ---------------------------------------------------


def strftime_example():

    while True:
        current_time = time.localtime()
        result = time.strftime("%I:%M:%S %p", current_time)
        print(result)
        time.sleep(1)




# iMPORTaNce !!! --------------------------------------------------------------------------------
# strftime(format, a_struct_time_object) function helps convert a struct_time object into a str
# Move you mouse to strftime function, docstring will tell you all the format usage
# -----------------------------------------------------------------------------------------------



# sleep_example()
# localtime_example()
strftime_example()
