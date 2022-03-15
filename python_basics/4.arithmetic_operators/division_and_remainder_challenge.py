# Divide Pens to Students

"""
* Problem Description

* Suppose you have to divide 14 pens among 3 students equally.

* How many pens will each student get if pens must be divided equally?

* And, how many pens will be left that cannot be divided?

* Task

* Create a variable named pens_number and assign 14 to it.

* Create a variable named students_number and assign 3 to it.

* Compute the number of pens each student will get and print it.

* Compute the number of pens that will be left and print it.
"""

# Solution

pens_number = 14

students_number = 3

#  number of pens each student will get

pensDevidedEqually = pens_number // students_number  # Finding the quotient (the int)

print('Number of pens each student will get:', pensDevidedEqually, 'pens')

# number of pens that will be left

pensLeft = pens_number % students_number  # Finding the remainder

print('Pens left that cannot be divided:', pensLeft, 'pens')
