class Mathematics:

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def minus(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def devide(x, y):
        return x / y




print('5 + 10 = ', Mathematics.add(5, 10))
print('5 - 10 = ', Mathematics.minus(5, 10))
print('5 * 10 = ', Mathematics.multiply(5, 10))
print('5 / 10 = ', Mathematics.devide(5, 10))

# IMPORTANCE !! --------------------------------------------
# 1) static method doesn't have self / cls as their 1st parameter, so it cannot reference any instance variables or class variables.
# 2) You can move any methods into a class, as long as you add @staticmethod annotation.
# ----------------------------------------------------------