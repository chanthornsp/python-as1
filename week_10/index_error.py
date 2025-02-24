try:
    numbers = [1, 2, 3, 4, 5]
    print(numbers[5])  # IndexError: list index out of range
except IndexError as e:
    print("Out of range index")