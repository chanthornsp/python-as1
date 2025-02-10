numbers = [1,5, 2, 3, 4, 5]

print(numbers, end='\n\n')
# numbers[0] = 10

for index in range(len(numbers)):
    numbers[index] = numbers[index] ** 2

print(numbers, end='\n\n')
numbers.append(10)
numbers.remove(25)
numbers.pop(-1)
print(numbers)

print('***********************', end='\n\n')
letters1 = ['a','b']
letters2 = ['x','y','z']
for letter1 in letters1:
    for letter2 in letters2:
        print(letter1 + letter2)

print('***********************', end='\n\n')

# Create a multplication table for numbers 1 to 9.

for i in range(1, 10):
    for j in range(1,11):
        print(i*j, end='\t')
    print() # print a new line
