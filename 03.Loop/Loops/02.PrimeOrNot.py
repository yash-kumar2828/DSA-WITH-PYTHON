# WAP to check the number is prime or not.

def isPrime(n):
    if n<2:
        return False
    elif n == 2:
        return True
    elif n%2 == 0:
        return False
    else:
        for i in range(3,int(n**0.5)+2):
            if n%i == 0:
                return False
        return True

num = int(input("Enter your number : "))

if isPrime(num):
    print(f"{num} is prime number")
else:
    print(f"{num} is not prime number")
    