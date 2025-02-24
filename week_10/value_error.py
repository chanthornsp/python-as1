while True:
    try:
        number = int(input('Enter number: '))
        print(number)
    except ValueError:
        print('Invalid value, try again!!!')