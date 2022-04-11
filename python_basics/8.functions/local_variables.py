def add_numbers(n1, n2):
    result = n1 + n2
    print(result)


add_numbers(2, 5)


# Trying to print the local variable
def add_numbers(n1, n2):
    result = n1 + n2


add_numbers(2, 5)
print(result)
