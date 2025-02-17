numbers = (1,2,3,4,5)
fruits = ('apple','banan','organge')
mixed = (1,2,3,'apple','banan','organge',True)

# Access by index
print(numbers[2])
print(fruits[2])
print(mixed[3])
print("end of access by index \n")

# Unpacking
person = ('sok',25,'Phnom Penh')
name,age,city = person
print(name)
print(age)
print(city)
print("end of unpacking \n")

# Tuple with 1 element 
number = (10,)
print(type(number))
real_number = (10)
print(type(real_number))
print("end of tuple with 1 element \n")

# Concatenation
numbers_and_fruits = numbers + fruits
print(numbers_and_fruits)
print("end of concatenation \n")

# Repeating 
repeated_numbers = numbers * 3
print(repeated_numbers)

# nested tuple
fruits_2 = ('apple','banana')
print(fruits_2[0])

nested = (1,2,fruits_2,3,4,numbers)
print(nested[2][1])
print("end of nested tuple \n")

# return multiple values
def get_person():
    name = 'Sok'
    age = 25
    city = 'Phnom Penh'
    return name, age, city

person = get_person()
print(person)  # Output: ('Sok', 25, 'Phnom Penh')
