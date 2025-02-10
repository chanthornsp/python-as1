import time

print("Generator Functions")
# using keyword yield

def countdown(number):
    while number > 0:
        yield number
        number -= 1 # number = number -1


# count_num = int(input('Enter number to countdown'))
count_num = 1

for i in countdown(count_num):
    time.sleep(1) # delay 1s
    print(i)

print("Higher-Order Functions")

def apply_operation(num1,num2,operation):
    return operation(num1,num2)

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2
i
def mul(num1,num2):
    return num1*num2

result = apply_operation(5,10,mul)
print(f"The result: {result}")