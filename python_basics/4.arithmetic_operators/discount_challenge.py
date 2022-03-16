"""
* Problem Description

*Suppose you are a university student and you need to pay 1536 dollars as a tuition fee.

*The college is offering a 10% discount on the early payment. How much money do you have to pay if you make an early payment?

*Task

*Create a variable named fee and assign 1536 to it.

*Create another variable discount_percent and assign 10 to it.

*Compute discount and assign it to the discount variable.

*Compute and print the fee you have to pay by subtracting discount from fee.
"""

fee = 1536

discount_percent = 10

discount = fee - (fee * 0.1)
fee = discount

print(fee)  # Output: 1382.4
