# Write a Python program to take a user input and print each
# digits of the number one by one from right to left.
# Input:
# N=43705
# Output:
# 5
# 0
# 7
# 3
# 4


def print_each_digit(num):
    while num>0:
        rem = num%10
        print(rem)
        num//=10

num = int(input("Enter your number : "))
print_each_digit(num)
