numbers = [1,3,4,5,6]
for number in numbers:
    print(number ** 2)

# Exercises 🏋️‍♂ and Solutions 💡
# 1. Print each letter in a string, separated by a hyphen.
word = "Hello Python"
for letter in word:
    if(letter != " "):
        print(letter, end="-")

print("\n")
print("2. Calculate the sum of all even numbers from 1 to 10.")
total = 0 # int value
for number in range(2,11,2):
    total += number
print(total)
print("\n")
print("3. Create a list of squared of numbers from 1 to 5.")

squared_numbers = [] # int value
for number in range(1,6):
    # print(number)
    squared_numbers.append(number **2)

print(squared_numbers)