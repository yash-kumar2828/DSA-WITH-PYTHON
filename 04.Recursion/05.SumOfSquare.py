# WAPP to print sum of squares of numbers from 1 to 100 by using recursion.

def get_sum_square(n):
    if n == 1:
        return 1
    return (n**2)+get_sum_square(n-1)

num = int(input("Enter your number : "))
sumOfSquare = get_sum_square(num)
print("Sum of square number is : ",sumOfSquare)