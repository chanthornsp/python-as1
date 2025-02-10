# define a function to calculate the area of a rectangle
def calculate_area(length,width):
    """function to calculate the area of a rectangle"""
    return length * width

print(calculate_area(5,5))

def add_numbers(num1,num2,num3):
    """function add numbers"""
    result = num1 + num2 + num3
    print(result)

# call function
add_numbers(5,5,10)

print('*********scope of variables*********')

def my_function():
    x = 10
    print(x)

my_function()
# print(x)

y = 20
def my_function2():
    print(f"My function2 {y}")

my_function2()
print(y)

print('*********default arguments*********')

def greet_user(name,greeting='Hello'):
    print(f"{greeting} {name}")
# call function
greet_user('Sok san','Good morning')

print('Function with Variable Number of Arguments (Arbitrary Arguments)')

def calculate_sum(*args):
    # print(type(args))
    return sum(args)

print(calculate_sum(1,2,3,4,56,3,54,6))

print("Function with Keyword Arguments")

def person_info(name,age,country):
    print(f"Name: {name}, Age: {age}, Country: {country}")

# call function
person_info(name="sok san",age=25,country="Cambodia")
person_info(age=25,country="Cambodia",name="Piset")