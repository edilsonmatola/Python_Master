"""
* Create a function to compute the factorial of a number. 
"""


def compute_factorial(n):
    factorial = 1

    # computer factorial
    for i in range(1, n + 1):
        factorial = factorial * i

    # return factorial
    return factorial


# Get user input
number = int(input('Insert the factorial number: '))

total = compute_factorial(number)

print(total)
