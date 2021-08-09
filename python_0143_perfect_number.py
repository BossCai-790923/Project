def Perfect_Number(num):
    result = []
    for i in range(1, num):
        list1 = []
        for x in range(1, i):
            if i % x == 0:
                list1.append(x)
        list1sum = sum(list1)
        if list1sum == i:
            result.append(list1sum)
    print(result)


Perfect_Number(1000)


def find_all_primes(upper_boundary):
    prime_list = []

    for prime_candidate in range(2, upper_boundary + 1):
        # When I code here, I notice I can define another function, to t
        if is_prime(prime_candidate):
            prime_list.append(prime_candidate)

    print(prime_list)


def is_prime(prime_candidate):
    '''
    tell whether prime_candidate is a prime number or not
    :param prime_candidate:
    :return: True if prime_candidate is a prime number
    '''
    for potential_factor in range(2, prime_candidate):
        if prime_candidate % potential_factor == 0:
            return False
    return True


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
          109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
          233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
          367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
          499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641,
          643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
          797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
          947, 953, 967, 971, 977, 983, 991, 997]
# 如果2^P-1是素数(其中指数P也是素数),则2^(P-1)(2^P-1)是完全数。
P = primes[0]


def sol2(num):
    for _ in range(len(primes)):
        P = primes[_]
        for i in range(len(primes)):
            for x in range(len(primes)):
                if 2 ** P - 1 == primes[i] and P == primes[x]:
                    print(2 ** (P - 1) * (2 ** P - 1))


sol2(1000)

'''
Requirement:
if a number equals to the sum of all of its factors (excluding itself), then the number is called a perfect number
6 is a perfect number, as 6 = 1 + 2 + 3.
Find all perfect number within 1000
Logic:
1) Find all numbers smaller than 1000, so it should be:
    for candidate in range(2, 1001):
        pass
2) For each candidate, we need to check whether it is a perfect number or not. To do that, we need to:
   2.1) Find all factors of the candidate. (1 included, itself not included)
        factor_list = []
        for potential_factor in range(1, candidate):
            if candidate % potential_factor == 0:
                factor_list.append(potential_factor)
   2.2) Check whether their sum equals to candidate or not
        we can just use built-in function sum()
'''

for candidate in range(2, 1001):

    factor_list = []
    for potential_factor in range(1, candidate):
        if candidate % potential_factor == 0:
            factor_list.append(potential_factor)

    if sum(factor_list) == candidate:
        print(candidate)
