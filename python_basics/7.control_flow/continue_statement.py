"""
*The continue statement skips the code inside the loop for that current iteration. The loop will not terminate but continues on with the next iteration.
"""

# Example:

for number in range(1, 11):

    # condition to check odd number
    if number % 2 != 0:
        continue

    print(number)
