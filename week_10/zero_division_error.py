while True:
    try:
        number = int(input('Enter a number: '))
        # if(number == 0):
        #     print('Can not divide by zero')
        #     continue # 
        print(10/number)
    except ZeroDivisionError as e:
        print("You can't divide by zero!")

