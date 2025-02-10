import math_operations as math_ops
import string_operations as string_ops
import utility_functions as utility
from art import grou_name,logo

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main_menu():
    while True:
        print("======= Main Menu=======")
        print(grou_name)
        print(logo)
        print("1. Math Operations")
        print("2. String Operations")
        print("3. Utility fuctions")
        print("4. Exit")
        choice = get_int_input("Enter your choice (1-4): ")

        if choice == 1:
            math_menu()
        elif choice == 2:
            string_menu()
        elif choice == 3:
           utility_menu()
        elif choice == 4:
            print("Exiting...")
            break # exit the loop
        else:
            print("Invalid choice. Please enter a number between 1-4.")


# math menu

def math_menu():
    while True:
        print("=====Math operations===")
        # add, subtract, multiply, divide, power
        print('1. Add ')
        print('2. Subtract')
        print('3. Multiply')
        print('4. Divide')
        print('5. Power')
        print('6. Back to main menu')
        choice = get_int_input("Enter your choice(1-6)")

        if(choice == 6):
            print('back to main menu')
            break
        elif(choice == 1):
            print('Addition')
            num1 = get_float_input("Enter first number: ")
            num2 = get_float_input("Enter second number: ")
            result = math_ops.add(num1, num2)
            print(f"Result: {result}")
        elif(choice == 2):
            print('Subtraction')
            num1 = get_float_input("Enter first number: ")
            num2 = get_float_input("Enter second number: ")
            result = math_ops.subtract(num1, num2)
            print(f"Result: {result}")
        elif(choice == 3):
            print('Multiplication')
            num1 = get_float_input("Enter first number: ")
            num2 = get_float_input("Enter second number: ")
            result = math_ops.multiply(num1, num2)
            print(f"Result: {result}")
        elif(choice == 4):
            print('Division')
            num1 = get_float_input("Enter first number: ")
            num2 = get_float_input("Enter second numberolleH: ")
            result = math_ops.divide(num1, num2)
            print(f"Result: {result}")
        elif(choice == 5):
            print('Power')
            num1 = get_float_input("Enter first number: ")
            num2 = get_float_input("Enter second number: ")
            result = math_ops.power(num1, num2)
            print(f"Result: {result}")
        else:
            print("Invalid choice. Please enter a number between 1-6.")

def string_menu():
    while True:
        print("=========String Operations=========")
        # reverse_string, to_upper, to_lower, capitalize, title
        print('1. Reverse string')
        print('2. Convert to upper case')
        print('3. Convert to lower case')
        print('4. Capitalize')
        print('5. Title')
        print('6. Back to main menu')
        choice = get_int_input("Enter your choice(1-6): ")

        if(choice == 1):
            print('Reverse string')
            string = input("Enter a string: ")
            result = string_ops.reverse_string(string)
            print(f"Result: {result}")
        elif(choice == 2):
            print('Convert to upper case')
            string = input("Enter a string: ")
            result = string_ops.to_upper(string)
            print(f"Result: {result}")
        elif(choice == 3):
            print('Convert to lower case')
            string = input("Enter a string: ")
            result = string_ops.to_lower(string)
            print(f"Result: {result}")
        elif(choice == 4):
            print('Capitalize')
            string = input("Enter a string: ")
            result = string_ops.capitalize(string)
            print(f"Result: {result}")
        elif(choice == 5):
            print("Title")
            string = input("Enter a string: ")
            result = string_ops.title(string)
            print(f"Result: {result}")
        elif(choice == 6):
            print("Back to main menu")
            return
        else:
            print("Invalid choice. Please enter a number between 1-6.")

def utility_menu():
    starting = True
    while starting:
        print('=======Utility Functions======')
        print('1. Get current time')
        print('2. Generate random number')
        print('3. Generate OTP number')
        print('4. Back to main menu')
        choice = get_int_input('Enter your choice(1-4): ')
        
        if choice == 1:
            print("Get Current time")
            print(f"Current time: {utility.get_current_time()}")
        elif choice == 2:
            print("Generate random number")
            start = get_int_input("Enter start: ")
            end = get_int_input("Enter end: ")
            print(f"Random number: {utility.generate_random_number(start=start, end=end)}")
        elif choice == 3:
            print("Generate OTP number")
            print(f"OTP number: {utility.generate_otp_number()}")
        elif choice == 4:
            print("Back to main menu")
            starting = False
        else:
            print("Invalid choice. Please enter a number between 1-4.")

# starting the program
if __name__ == "__main__":
    main_menu()