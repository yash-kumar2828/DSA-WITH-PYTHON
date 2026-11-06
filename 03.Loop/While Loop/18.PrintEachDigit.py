# Write a python program to take a user input and print
# each digit of the number from left to right.
# Input:
# N=43705
# Output:
# 4
# 3
# 7
# 0
# 5


def print_each_digit(num):
    if num == 0:
        print(0)
    else:
        divisor = 1
        temp = num
        while temp >= 10:
            divisor *= 10
            temp //= 10
    
        temp = num
        while divisor > 0:
            digit = temp // divisor
            print(digit)
            temp %= divisor  
            divisor //= 10      

num = int(input("Enter your number : "))
print_each_digit(num)