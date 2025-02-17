
# Create list as int

numbers = [1,2,3,4,5,6,7,8,9,10]
# Create list as string
fruits = ['apple','banan','organge']

# mixed list 
mixed_list = [1,2,3,'apple','banan','organge',True]

# access by index
print(numbers[-1]) # reverse index
print(fruits[1])
print(mixed_list[3])

#modify list
fruits[0]= 'Kiwi'
print(fruits)

# Add new list at the end
fruits.append('Watermelon')
print(fruits)

# add new list with specific position by index
fruits.insert(1,'Strawberry')
print(fruits)



# remove by value
fruits.remove('organge')
print(fruits)

# remove by index
fruits.pop(1)
print(fruits)

# slicing
sub_numbers = numbers[1:9:2] # start: 1, end: 9, step: 2
print(sub_numbers)

# List comprehension to create a new list
squared_numbers = [num**2 for num in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
