import math
import random
from datetime import datetime
from time import sleep

print(math.sqrt(16))
print(math.factorial(5))

print(random.randint(1,100))

while True:
    print(datetime.now().strftime("%d-%m-%Y, %H:%M:%S"))
    sleep(1)