# Lists are one of the most versatile data types that allow us to work with multiple elements.

# A list is created by placing items(elements) inside square brackets[], separated by commas. For example,


# empty list
list1 = []
print(list1)   # Output: []

# list of integers
numbers = [1, 2, 3]
print(numbers)   # Output: [1, 2, 3]

# list with mixed data types
mixed_list = [1, "Hello", 3.4]
print(mixed_list)   # Output: [1, 'Hello', 3.4]

# list with duplicate items
list2 = [1, 2, 3, 1, 3]
print(list2)   # Output: [1, 2, 3, 1, 3]


"""
* Acessing List Items
"""

languages = ['Python', 'Dart', 'JavaScript', 'Java']

# First language
first_language = languages[0]
print(first_language)   # Output: Python

# Second language
second_language = languages[1]
print(second_language)   # Output: Dart

# Third language
third_language = languages[2]
print(third_language)   # Output: JavaScript


"""
* Negative Indexing
"""

# Third language
third_language = languages[-3]
print(third_language)   # Output: JavaScript

# Last language
last_language = languages[-1]
print(last_language)   # Output: 'Java'


"""
* CHALLENGE

Create a list containing 3 items: 9, 11, and 15, and assign it to the odd_numbers variable.
Print the second item of the list (using a positive index).
"""

odd_numbers = [9, 11, 15]

second_item = odd_numbers[1]
print(second_item)