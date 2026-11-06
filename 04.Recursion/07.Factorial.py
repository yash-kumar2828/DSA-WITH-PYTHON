# WAPP to calculate factorial by using recursion.

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

num = int(input("Enter your number : "))
fact = factorial(num)
print(f"Factorial of {num} is : {fact}")