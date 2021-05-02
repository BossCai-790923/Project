"""
Requirement: find all prime numbers less than 100, using for loop - break - else
"""
for prime_candidate in range(2,101):
    for potential_factor in range(2,prime_candidate):
        if(prime_candidate%potential_factor==0):
            print(f'{prime_candidate} is not a prime number')
            break
    else:
        print(prime_candidate,'is a prime number')