# Create Dictionary
student_info = {
    'name': 'Sok san',
    'age':25,
    'city':'Phnom Penh',
    'courses': ['Math','Science']
}
print(student_info)

# Access by key
name = student_info['name']
print(name)
courses = student_info['courses']
print(courses[0])

# modify
student_info['age'] = 30
print(student_info)

# add new-key value
student_info['gender'] = 'Male'
print(student_info)

# remove by key
student_info.pop('city')
print(student_info)

# Checking key exist

is_city = 'city' in student_info
print(is_city)
print('end of checking key exist \n')

# Loop key Dictionary
for key in student_info:
    print(key)
print('end of loop key \n')

# Loop value Dictionary
for value in student_info.values():
    print(value)
print('end of loop value \n')

# Loop key-value Dictionary
for key, value in student_info.items():
    print(f"{key}: {value}")

    # Dictionary comprehension to create a new dictionary
squared_numbers = {num: num**2 for num in range(1, 6)}
print(squared_numbers)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}