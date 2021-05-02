# What ever you define some variables
# First question is: What's the type of the variable

# IMPORTANCE!! -------------------------------------------------------
# U must be crystal clear of the var. type in your mind
# --------------------------------------------------------------------

a_int_var = 1   # int, because it is a natural number
a_float_var = 1.0  # float, because it has a decimal point
a_str_var = 'Hello' # str, because it is surrounded by single quote or double quotes
a_bool_var = True  # bool, because bool has only 2 values - True/False
# a_wrong_var = dog   #  wrong.

print(a_int_var, a_float_var, a_str_var, a_bool_var)
print('-------------------------------------------------------')


str_a = '10'        # this is of type 'str'
str_b = "10.2"      # this is of type 'str'
print(str_a, str_b)

# if i plus 2 str variables together, I am actually joining them together
str_c = str_a + str_b # str + str = str, so str_c is a str variable

print(f'join 2 string: "{str_a}" + "{str_b}" = "{str_c}"') # Join 2 str: "10" + "10.2" = "1010.2"
print('-----------------------------------------------------')


# IMPORTANCE!! -----------------------------------------------------
# int()   - convert variable to a int variable      - it has a special name 'int constructor'
# float() - convert variable to a float variable    - it has a special name 'float constructor'
# ------------------------------------------------------------------
int_a = int(str_a)       # convert str '10' to int 10
float_b = float(str_b)   # convert str '10.2' to float 10.2
print(f"{int_a}'s type is {type(int_a)}")            # 10's type is <class 'int'>
print(f"{float_b}'s type is {type(float_b)}")        # 10.2's type is <class 'float'>

# This line will cause a ValueError
# int_c = int("Hello")  # not all str values can be converted to int

float_c = int_a + float_b # int + float = float     so variable float_c is of type 'float'
print(f'Plus 2 numbers: {int_a} + {float_b} = {float_c}') # Plus 2 numbers: 10 + 10.2 = 20.2

print('-----------------------------------------------------------------')




# More example of int constructor int()---------------------------------

# IMPORTANCE!! ------------------------------------------------------
# When you pass a decimal value to the int constructor:
# It always tries shrinking the decimal value to the nearest natural number towards 0
# -------------------------------------------------------------------
int_a = int(2.1)    # 2
int_b = int(3.9)    # 3   not 4
int_c = int(-4.1)   # -4
int_d = int(-5.9)   # -5  not -5
int_e = int('6') #取整
print(int_a, int_b, int_c, int_d, int_e) # 2 3 -4 -5 6


# More example of float constructor float()
float_a = float(2)
float_b = float(3)
float_c = float("4")
print(float_a, float_b, float_c)  # 2.0 3.0 4.0