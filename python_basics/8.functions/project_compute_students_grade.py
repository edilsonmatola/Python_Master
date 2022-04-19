"""
* Suppose you are a teaching assistant in a University, and you need to assign grades to students based on their average scores.

* Your job is to first compute the average score first. And, based on the average score, you need to compute a student's grade.
* 
* The grading rule is like this:
* 
* Grade A if the average score is equal to or above 80
* Grade B if the average score is equal to or above 60 and less than 80
* Grade C if the average score is equal to or above 50 and less than 60
* Grade F if the average score is less than 50

"""

# Create a function to compute the average score


def compute_average_score(student_scores):
    total = sum(student_scores)
    average = total / len(student_scores)
    return average


# Create a function to compute the grade
def compute_grade(average_score):
    if average_score >= 80:
        grade = 'A'
    elif average_score >= 60 and average_score < 80:
        grade = 'B'
    elif average_score >= 50 and average_score < 60:
        grade = 'C'
    else:
        grade = 'F'
    return grade


# The scores
student_scores = [55, 64, 75, 80, 65]

average_score = compute_average_score(student_scores)

grade = compute_grade(average_score)

print('Average score is',  average_score)
print('Grade:', grade)
