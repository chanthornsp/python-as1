try:
    result = 10 + "10"
    print(result)
except TypeError as e:
    print(e)
    # print('You can not add a number to a string!!')