"""

* Create a program to check whether a number is positive or negative or zero.

* Get integer input from the user and store it in the number variable.

* If number is positive, print positive.

* If number is negative, print negative.

* If number is 0, print zero.

"""

number = int(input('Insert an integer number: '))

if number > 0:
    print('Positive')
elif number < 0:
    print('Negative')
else:
    print('Zero')
