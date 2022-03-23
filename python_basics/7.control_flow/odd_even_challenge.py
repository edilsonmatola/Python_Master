"""
* Create a program to check whether a number is even or odd.

* Get integer input from the user and store it in the number variable.

* If number is even, print even.

* If number is odd, print odd.

* Hint: A number is even if the remainder is 0 when it's divided by 2. Basically, if number % 2 is equal to 0, the number is even.

"""

number = int(input('Insrt an integer number: '))

if number % 2 == 0:
    print('even')
else:
    print('odd')
