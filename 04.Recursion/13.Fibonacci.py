# WAPP to calculate nth term of Fibonacci series by using recursion.

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibo(n-1)+fibo(n-2)


num = int(input("Enter your number : "))
for i in range(num):
    print(fibo(i),end=" ")

    