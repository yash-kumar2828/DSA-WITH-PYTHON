# Write a python program to take a user input
# and print the sum of each even digits of
# the number.
# Input:
# N=42765
# Output:
# 12

def sum_of_even_digit(num):
    evenSum = 0
    while num>0:
        rem = num%10
        if rem%2==0:
            evenSum+=rem
        num//=10
    print(f"The sum of even digit is : {evenSum}")

num = int(input("Enter your number  : "))
sum_of_even_digit(num)