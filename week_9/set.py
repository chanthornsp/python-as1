# Creating sets
from operator import is_


numbers = {1,2,3,4,5}
fruits = {'apple','banan','organge'}
colors = set(['red','green','blue'])
print(fruits)
# Adding new element
fruits.add('kiwi')
print(fruits)

# remove element
fruits.remove('organge')
print(fruits)
print("end of remove element \n")

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set3= {1,2,3,9,10,11}

# Union two sets
union_set = set1.union(set2,set3)
print(union_set) #
print("end of union set \n")

# Intersection
intersection_set = set1.intersection(set2)
print(intersection_set)

# Difference 
difference_set = set1.difference(set2) # set1 difference set2
print(difference_set)

# Symmetric difference
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)
print("end of symmetric difference \n")

# is subset
is_subset = set1.issubset(set2)
print(is_subset)
set4 = {1,2,3}
set5 = {1,2,3,4,5,6,7,8,9,10}
is_subset = set4.issubset(set5)
print(is_subset)
print("end of is subset \n")

# Comprenhension
numbers = {1, 2, 3, 4, 5}

# Set comprehension to create a new set
squared_numbers = {num**2 for num in numbers}
print(squared_numbers)  # Output: {1, 4, 9, 16, 25}
print("end of set comprehension \n")

numbers = [1,2,3,4,3,5,3,6,7,5,4,8,9,10]
unique_numbers = set(numbers)
print(unique_numbers)