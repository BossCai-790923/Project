
'''
brute force means: try all possibilities
brute force simply takes advantage of the computer power to exhaust all possibilities
brute force does not implement any optimization, or implement very limited optimization
brute force is a BAD algorithm
brute force takes a long time
brute force is the last choice
'''


#solution 1: brute force - O(n^2)
def solution1_brute_force(upper_bound):
    check_times = 0
    prime_number_list = []

    for prime_candidate in range(2, upper_bound):

        # brute force - check till prime_candidate
        for potential_factor in range(2, prime_candidate):
            check_times += 1
            if prime_candidate % potential_factor == 0:
                break
        else:
            prime_number_list.append(prime_candidate)

    print(check_times)
    print(prime_number_list)


#solution 2 - check till square root
def solution2_check_till_sqrt(upper_bound):
    check_times = 0
    prime_number_list = []

    for prime_candidate in range(2, upper_bound):
        #optimized - check till the square root of prime_candidate
        sqrt_of_number_to_be_checked = int(prime_candidate ** 0.5) + 1
        #brute force - check till prime_candidate
        for potential_factor in range(2, sqrt_of_number_to_be_checked):
            check_times += 1
            if prime_candidate % potential_factor == 0:
                break
        else:
            prime_number_list.append(prime_candidate)
    print(check_times)
    print(prime_number_list)

#HOMEWORK: Explain clearly, why if we check till square root, it is already good enough?
# solution 3 - check all primes till square root
def solution3_check_prime_till_sqrt(upper_bound):
    check_times = 0
    prime_number_list = []
    for prime_candidate in range(2, upper_bound):
        # optimized - check till the square root of prime_candidate
        sqrt_of_number_to_be_checked = int(prime_candidate ** 0.5) + 1
        # traditional way ------------------------------------
        # prime_to_be_checked = []
        # for prime in prime_number_list:
        #     if prime <= sqrt_of_number_to_be_checked:
        #         prime_to_be_checked.append(prime)
        # list comprhension
        prime_to_be_checked = [prime for prime in prime_number_list if prime <= sqrt_of_number_to_be_checked]

        # brute force - check till prime_candidate
        for potential_factor in prime_to_be_checked:
            check_times += 1
            if prime_candidate % potential_factor == 0:
                break
        else:
            prime_number_list.append(prime_candidate)

    print(check_times)
    print(prime_number_list)

