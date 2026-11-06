# WAPP to print sum of numbers from 1 to 100 by using recursion.

def getSum(n):
    if n == 1:
        return 1
    return n+getSum(n-1)


num = int(input("Enter your number : "))
sum = getSum(num)
print("Sum of all number is : ",sum)
