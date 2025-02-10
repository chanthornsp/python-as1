x = 10
if x > 5:
    print("x is greater than 5")


if x % 2 == 0:
    print("x is even number")
else:
    print("x is odd number")

if x > 0:
    print("x is positive number")
elif x < 0:
    print("x is negative number")
else:
    print("x is zero")


y = 5

if x > 5:
    if y > 5:
        print("x and y are greater than 5")
    else:
        print("x is greater than 5 but y is less than or equal 5")        
else:
    print('x is less than or equal to 5')