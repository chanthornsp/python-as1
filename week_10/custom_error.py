class CustomError(Exception):
    pass

def divide(a,b):
    if(b==0):
        raise CustomError('Can not divide by zero!!')
    return a / b

try:
    print(divide(10,0))
except CustomError as e:
    print(e)