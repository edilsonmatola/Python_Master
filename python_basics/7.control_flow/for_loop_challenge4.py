"""
* Create a program to print odd numbers between 1 and n (entered by the user).

* Get an integer input from the user. We will assume the user will enter a positive integer.

* Using a loop iterate from 1 to n (n should be inclusive).

* In each iteration of the loop, print the number if it's an odd number.

"""

n = int(input('Enter a number: '))

for number in range(1, n + 1):
    if number % 2 != 0:
        print('Odd number(s):', number)
