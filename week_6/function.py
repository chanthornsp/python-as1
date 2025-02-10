def factorial(n):
    """Calculate the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Call the function

# num = int(input("Enter a number: "))
num = 5
result = factorial(num) # 5! = 5*4*3*2*1 = 120
print(result) # Output: 120

print("Returning Multiple Values")

def calculate_values(num1,num2):
    """Calculate the sum and product of two numbers."""
    sum = num1 + num2
    product = num1 * num2
    return sum, product

# Call the function
s,p = calculate_values(5,10)

print(f"Sum: {s}, Product: {p}")

print("Lambda Functions (Anonymous Functions) (Anonymous Functions))")

add = lambda num1,num2: num1 + num2

print(add(5,10))

