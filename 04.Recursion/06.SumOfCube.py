# WAPP to print sum of cubes of numbers from 1 to 100 by using recursion.

def sum_cube_number(n):
    if n == 1:
        return 1
    return (n**3)+sum_cube_number(n-1)

num = int(input("Enter your number : "))
sumCubeNumber = sum_cube_number(num)
print("Sum of cube number is : ",sumCubeNumber)