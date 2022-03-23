# Get student grade from the user
student_grade = int(input('Enter grade: '))

# condition for invalid score
if student_grade > 100 or student_grade < 0:
    print('Invalid grade.')
elif student_grade >= 50:   # if is changed to elif
    print('You passed.')
else:
    print('You failed.')
