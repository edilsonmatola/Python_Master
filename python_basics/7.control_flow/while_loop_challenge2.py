"""

* Factorial of a Number

* Create a program to find the factorial of an integer entered by the user.

* The factorial of a positive integer n is equal to 1 * 2 * 3 * ... * n. For example, the factorial of 4 is 1 * 2 * * 3 * 4 which is 24.

* Take an integer input from the user and assign it to the variable n. We will assume the user will always enter a  positive integer.

* Using a while loop, compute the factorial.

* Print the factorial at the end.


"""

number = int(input('Enter a number: '))

# The initial value of total is 1
total = 1

# counter
i = 1

while i <= number:
    total = total * i

    i += 1

print(total)
