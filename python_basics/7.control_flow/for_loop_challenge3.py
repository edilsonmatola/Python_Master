"""

Create a program to find the factorial of an integer entered by the user.

The factorial of a positive integer n is equal to 1 * 2 * 3 * ... * n. For example, the factorial of 4 is 1 * 2 * 3 * 4 which is 24.

Take an integer input from the user and assign it to the variable n. We will assume the user will always enter a positive integer.
Using a for loop, compute the factorial.
Print the factorial at the end. 


"""


# Take integer input
n = int(input())

# The initial value of total is 1
total = 1

for i in range(1, n):
    # multiply total and i in each iteration
    total = total * i

print(total)
