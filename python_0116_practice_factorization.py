'''
Requirement:
factorize number x (2 <= x <= 1000), print out the result.
For example:
When user inputs 90, your program should print:
90 = 2 * 3 * 3 * 5
'''

'''
Key logic:
Find out all prime numbers below 1000, try all prime numbers smaller than x.
Then I can find all the prime factors of x.
Step 1) Find out all prime numbers with 1000, put into list prime_list
        I define a function:
        def find_all_primes(upper_boundary):
            pass

Step 2) Find out all prime factors of x using prime_list, put the prime factors into list prime_factors
        I define a function:
        def find_all_prime_factors(x, prime_list):
            pass 

Step 3) Print out the result using number x and its prime_factors      
        I define a function:
        def print_result(x, prime_factors):
            pass                 
'''


def find_all_primes(upper_boundary):
    '''
    This finds all prime numbers smaller than upper_boundary
    :param upper_boundary:
    :return: a list of prime numbers smaller than upper_boundary
    '''
    prime_list = []

    for prime_candidate in range(2, upper_boundary + 1):
        # When I code here, I notice I can define another function, to tell whether prime_candidate is a prime_number or not
        if is_prime(prime_candidate):
            prime_list.append(prime_candidate)

    return prime_list

def is_prime(prime_candidate):
    '''
    tell whether prime_candidate is a prime number or not
    :param prime_candidate:
    :return: true if prime_candidate is a prime number
    '''
    for potential_factor in range(2, prime_candidate):
        if prime_candidate % potential_factor == 0:
            return False
    return True

# code for a while, test for a while
# my_prime_list = find_all_primes(20000)
# print(my_prime_list)


def find_all_prime_factors(x, prime_list):
    prime_factors = []

    for prime in prime_list:
        # because x can contain multiple same prime factor, so we have to use 'while' loop
        while x % prime == 0:
            # prime is a prime factor of x, so we add prime to list prime_factors
            prime_factors.append(prime)
            # remove prime from x
            x = x // prime

    return prime_factors


# Code for a while, test for a while
# my_prime_list = find_all_primes(1000)
# prime_factors = find_all_prime_factors(999, my_prime_list)
# print(prime_factors)
# prime_factors = find_all_prime_factors(7, my_prime_list)
# print(prime_factors)


def print_result(x, prime_factors):
    print(x, '=', end=' ')

    if len(prime_factors) == 1:
        print(1, "*", end=' ')

    # solution 1 asterisk unpacking
    # if prime_factor is a list containing [2, 3, 3, 5]
    # This equals to
    # print(2,3,3,5, sep= ' * ')
    print(*prime_factors, sep=' * ')

    # solution 2 list comprehension
    # print(' * '.join(str(elem) for elem in prime_factors))


# --------------------------------------------------------
# Now all basic functions have been implemented.
# Let's start our actual code.
# --------------------------------------------------------

prime_list = find_all_primes(1000)

x = int(input("X = "))
prime_factors = find_all_prime_factors(x, prime_list)

print_result(x, prime_factors)