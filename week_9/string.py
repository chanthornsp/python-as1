# Create string
single_quote = 'Hello, World!'
double_quote = "Hello, World!"

multi_line = """Hello,
World!
Welcome to Python Programming!"""

print(multi_line)
print("end of create string \n")

# Access by index
print(single_quote[1])
print(double_quote[-2])

# Slicing
print(single_quote[7:12]) # [start:stop:step]
print('end of slicing \n')

# Concatenation
first_name = "Sok"
last_name = "San"
title = "Mr."
full_name = title + " " + first_name + " "+last_name
print(full_name)

# Count string
print(full_name.count('S'))
print(len(full_name))

# String method
print(full_name.upper())
print(full_name.lower())
print(full_name.capitalize())
print(full_name.title())

# String format
full_name = f"{title} {first_name} {last_name}"
print('end of string format \n')

# escape character
message = 'Hello, \'World\'!'
print(message)
escaped_string = 'This is a\nmultiline string'
print(escaped_string)

# String repetition
message = 'Hello, '
repeated_message = message * 3
print(repeated_message)  # Output: Hello, Hello, Hello,