try:
    number_input = int(input('Enter a number: '))
    print('The number entered is:', number_input)
except Exception as e:
    print(f'An error occurred: {e}')
else:
    print('No Errors')
finally:
    print('This is the end of the program')