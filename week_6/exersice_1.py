# Exercise: Grade Calculator
# Write a Python program that performs the following tasks:
# 1. Define a function called calculate_average that takes a list of grades as input and returns the average.
# 2. Define a function called calculate_letter_grade that takes a numerical grade as input and returns the corresponding letter grade.
# 3. Create a list of student grades (you can use random grades for testing).
# 4. Calculate the average grade of the students using the calculate_average function.
# 5. For each student, print their numerical grade, letter grade, and whether they passed or failed (grade >= 60).

import random

# 1. Define calculate_average function
# average = sum of all grades / number of grades
def calculate_average(grades):
    return sum(grades)/len(grades)

# 2. Define calculate_letter_grade function
def calculate_letter_grade(grade):
    if 90 <= grade <= 100:
        return 'A'
    elif 80 <= grade < 90:
        return 'B'
    elif 70 <= grade < 80:
        return 'C'
    elif 60 <= grade < 70:
        return 'D'
    else:
        return 'F'
    
# 3. Create a list of student grades

student_grades = [random.randint(1,100) for i in range(10)]

# 4. Calculate the average grade of the students
average_grade = calculate_average(student_grades)

# 5.1 print the numerical grade, letter grade, and pass/fail status

for i,grade in enumerate(student_grades,1):
    letter_grade = calculate_letter_grade(grade)
    status = 'Passed' if grade >= 60 else 'Failed'
    print(f"Student {i}: {grade} ({letter_grade}) - {status}")

# 5.2 print the average grade

print(f"Average grade of all students: {average_grade:.2f}") 