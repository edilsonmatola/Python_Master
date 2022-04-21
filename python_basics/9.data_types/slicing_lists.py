"""
* Many times, we need to access a portion of the list, not just a single item.

* To get a sublist of a list, we can use the : notation.

"""

numbers = [10, 20, 30, 40, 50, 60]

# Slicing the list
print(numbers[1:4])  # Output: [20, 30, 40]

# The one thing we need to remember about slicing is that the start index is inclusive, but the end index is exclusive.

# Print items from index 0 to index 3 (not including index 4)
print(numbers[0:4])  # Output: [10, 20, 30, 40]

# Print items from index 3 to 5
print(numbers[3:5])  # Output: [40,
