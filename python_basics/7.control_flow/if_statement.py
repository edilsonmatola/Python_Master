# Check whether a student passed or failed the exam.
# We will assume the passing grade is 50 or above.

# Get student score from the user
student_grade = int(input('Enter grade: '))

# If student_grade is 50 or above,
# student_grade >= 50 results to True
if student_grade >= 50:
    print('Congratulations!')
    print('You passed the examination.')
