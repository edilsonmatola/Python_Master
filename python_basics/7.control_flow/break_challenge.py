"""
* Problem Description

* Create a program to calculate the sum of integers entered by the user. If the user enters 0 or negative integer, terminate the loop and print the sum.


* Initialize a variable named total with value 0 at the beginning.

* Create a while loop with condition True.

* If the user enters 0 or negative integer, use break to terminate the loop.

* If the user enters a positive number, add it to the total variable.

* Print the total from outside of the loop.

"""

total = 0

while True:
    number = int(input())

    if number == 0 or number < 0:
        break

    total += number

print(total)
