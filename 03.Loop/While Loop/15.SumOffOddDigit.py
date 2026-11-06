# Write a python program to take a user input
# and print the sum of each odd digits of
# the number.
# Input:
# N=42763
# Output:
# 10

def sum_of_odd_digit(num):
    oddSum = 0
    while num>0:
        rem = num%10
        if rem%2 == 1:
            oddSum+=rem
        num//=10
    print(f"The sum of odd digit is : {oddSum}")

num = int(input("Enter your number : "))
sum_of_odd_digit(num)