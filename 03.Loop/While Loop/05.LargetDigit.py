# Write a pytjon program to take a user input
# and print the biggest digit of the number.
# Input:
# N=43705
# Output:
# 7

def largest_digit(num):
    largest = 0
    while num>0:
        rem = num%10
        if rem>largest:
            largest = rem
        num//=10
    print(largest)

num = int(input('Enter your number : '))
largest_digit(num)