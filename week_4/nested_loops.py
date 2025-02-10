# Example 1 nested for loop in Python
numbers = [1,2,3,4,5]
letters = ['a','b']

for num in numbers:
    # print(num)
    for letter in letters:
        print(num,letter)

# Example 2 while loop with nested loop
print("Example 2")
count = 0
while count < 3:
    for num in range(1,4):
        print(count,num)
    count +=1


# Example 3
print("Example 3")
numbers = [1,2,3]
count = 0
for num in numbers:
    while count < 3:
        print(num,count)
        count +=1
    count = 0