# 3. Write a program that finds all prime numbers up to a given number.

def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2,int(num ** 0.5) +1):
        if num % i == 0:
            return False
        
    return True

def find_prime(limit):
    primes = []
    for num in range(2,limit+1):
        if(is_prime(num)):
            primes.append(num)
    return primes


limit = 26
primes = find_prime(limit)

print(f"Prime numbers up to {limit}: {primes}")
         