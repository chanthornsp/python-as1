# Even or Odd Number: Write a Python program that takes an integer as input and prints
#  whether the number is even or odd.

print("Even or Odd Number checker")
x = int(input("Enter a number:"))
if x % 2 == 0:
    print("x is even number")
else:
    print("x is odd number")

# Simple Login System: Write a Python program that takes a username and password as input.
#  If the username is "admin" and the password is "password123",
#  print "Login successful". Otherwise, print "Login failed".
# Hint: Use nested if statements to check both the username and password.
print("Simple Login System")

username = input("Enter your username:")
password = input("Enter your password:")

if username == "admin":
    if password == "password123":
        print("Login successful")
    else:
        print("Login failed")
else:
    print("Wrong username")