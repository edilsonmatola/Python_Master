"""

*Problem Description

*Check whether a person can vote or not depending upon his/her age.

*Get integer input from the user and store it in the age variable.

* If age is 18 or above, print The person can vote. If not, print The person cannot vote.

"""

age = int(input('Insert your age: '))

if age >= 18:
    vote = 'The person can vote.'
else:
    vote = 'The person cannot vote.'

print(vote)
