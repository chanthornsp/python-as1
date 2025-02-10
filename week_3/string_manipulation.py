first_name = "sok"
last_name = "san"
age = 25

# full_name = first_name + " " + last_name
full_name = f"{first_name} {last_name}" #sok san
# print (full_name + " is " + str(age))
# print(full_name)

greeting = f"Hello, my name is {full_name}, and I am {age} years old."
# print(greeting)

#length  of strings
# print(len(full_name))

#Accessing Individual Characters
first_char_full_name = full_name[0]
print(first_char_full_name)
k_from_full_name = full_name[2]
print(k_from_full_name)

# last char
last_char = full_name[len(full_name) -1]
print(last_char)
print(full_name[-1])

#Slicing

print(greeting[0:5])

# Conversion

to_upper_case = full_name.upper()
print(to_upper_case)
to_lower_case = full_name.lower()
print(to_lower_case)
to_title_case = full_name.title()
print(to_title_case)

# remove white space 
text = "        Hello, World!        "
print(text.strip())


# replace 
text = "Hello, World!"
hello_python = text.replace("World","Python")
print(hello_python)

constain_hello = "Hello" in text
print(constain_hello)

# splite
fruits = "apple,banana,orange"
fruits_list = fruits.split(",")

print(type(fruits))
print(fruits_list)

