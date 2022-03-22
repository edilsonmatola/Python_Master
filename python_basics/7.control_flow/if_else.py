# Get student score from the user

student_grade = int(input('Enter grade: '))

if student_grade >= 50:
    print('Congratulations!')
    print('You passed the examination.')
else:
    print('Sorry.')
    print('You failed the examination.')

# Always executed because it's outside if...else
print("Don't you think Python is fun?")
