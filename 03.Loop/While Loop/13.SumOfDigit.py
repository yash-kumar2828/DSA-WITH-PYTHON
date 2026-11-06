# Write a python program to take a user input
# and print the sum of each digit of the
# number.
# Input:
# N=4207065
# Output:
# 24

def sum_of_digit(num):
    sum = 0
    while num>0:
        rem = num%10
        sum+=rem
        num//=10
    print(f"The sum of digit is : {sum}")

num= int(input("Enter your number : "))
sum_of_digit(num)