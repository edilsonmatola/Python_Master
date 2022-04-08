"""
* Create a program to print odd numbers between 1 and n, where n is a positive integer entered by the user.

* 
Take integer input from the user and store it in variable n.
* 
Use a for loop to iterate from number equal to 1 to n+1.
* 
If number is even, use continue to skip the number from printing.
* 
If number is odd, print the number.

"""

number = int(input('Insert a number: '))

for n in range(1, number + 1):
    if n % 2 == 0:
        continue
    print(n)
