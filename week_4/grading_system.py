# Grading System
# Write a Python program that takes a numerical grade as input and prints the corresponding letter grade based on the following scale:

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59
# The User should input marke between 0-100.
# Hint: Use the if-elif-else statement to check the grade range.
print("Grading System")
mark = float(input("Enter your mark: "))
if mark > 100 or mark < 0:
   grade = "Invalid mark"	
elif mark >= 90:
    grade = "A"
elif mark >= 80:
    grade = "B"
elif mark >=70:
    grade = "C"
elif mark >= 60:
    grade = "D"	
else:
    grade = "F"

print(grade)