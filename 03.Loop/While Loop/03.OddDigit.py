# Write a python program to take a user input
# and print each odd digits of the number
# one by one.
# Input:
# N=43705
# Output:
# 5
# 7
# 3

def print_odd_digit(num):
    while num>0:
        rem = num%10
        if rem%2!=0:
            print(rem)
        num//=10

num = int(input("Enter your number : "))
print_odd_digit(num)