'''
find the value of s
s = a + aa + aaa + aaaa + aa...a，
a can be any number from 1 to 9
term count comes from user input in console.
For example:
Enter the base number: 2
Enter the term count: 5
The answer is 24690
Explanation:
2 + 22 + 222 + 2222 + 22222 is 24690
'''


# Observation
# term 0 - 5
# term 1 - 55 = 5 * 10 + 5
# term 2 - 555 = 5 * (5 * 10 + 5) + 5
# term 3 - 5555 = 5 * (5 * (5 * 10 + 5) + 5) + 5

# Summary
# term 0 = Loop 0 times [* 10 + 5]
# term 1 = Loop 1 times [* 10 + 5]
# term 2 = Loop 2 times [* 10 + 5]
# term 3 = Loop 3 times [* 10 + 5]

def solution1_math(base_number, term_count):
    sum_ = 0
    for term_no in range(term_count):
        term_value = base_number

        for _ in range(term_no):
            term_value = term_value * 10 + base_number

        sum_ += term_value

    return sum_


'''
Question:
How many times the calculate (line 35) will be executed?
Let's say, in total we have n terms.
Answer: 1 + 2 + 3 ... + n
      = (1 + n) * n / 2
      = 1/2 * n^2 + 1/2 * n

Time Complexity: O(n^2)
-----------------------------------------------------------------------------------
Time Complexity means: how code slows as data grows
Time Complexity answer this question: how much slower the code will go if you give it ten times more data.
We use Big-O to express this.
When n = 10;  it calculate = 1/2 * 10 * 10     + 1/2 * 10   = 50    + 5  = 55   times      
When n = 100; it calculate = 1/2 * 100 * 100   + 1/2 * 100  = 5000  + 50 = 5050 times - when data grows 10 times, roughly, code slows 100 times.      
The driven factor is n^2, (1/2 * n) can be ignored.
So we say: Big-O(n^2)
O(1)
O(n)
O(n^2)
'''


# solution 1 can be optimized

# term 0 - 5\
# term 1 - 55 = (term 0 * 10) + 5\
# term 2 - 555 = (term 1 * 10) + 5\

def solution2_math_optimized(base_number, term_count):
    sum_ = 0

    term_value = base_number  # put term 0 into sum
    sum_ += term_value

    for _ in range(term_count - 1):  # repeat term_count - 1 times, since we start from term 1
        term_value = term_value * 10 + base_number  # calculate the next value of 'term_value'
        sum_ += term_value  # add to sum

    return sum_

'''
question:
how many times the calculate will be executed
let's say ,intotal we have n terms
answer:n-1
time complexity :O(n)
when n=10,it calculates10-1=9times
when n=100,it calculates100-1=99times
so,when data grows 10 times,roughly,code slows 10 times.
the driving factor is n,-1 can be ignore
so we say big-O(n)

'''

def solution7_eval(base_number, term_count):
    '''
    Tte idea is to build the expression directly.
    and I use built-in function eval(expression) to calculate the result directly
    '''
    expression = ''
    for i in range(1, term_count + 1):
        expression += str(base_number) * i
        if i < term_count:
            expression += '+'
    print("here comes the expression:", expression)
    sum_ = eval(expression)
    return sum_

base_number = int(input("Enter the base number: "))
term_count = int(input("Enter the term count: "))

result = solution1_math(base_number, term_count)
print("The answer is: ", result)

result = solution2_math_optimized(base_number, term_count)
print("The answer is: ", result)

result = solution7_eval(base_number, term_count)
print("The answer is: ", result)