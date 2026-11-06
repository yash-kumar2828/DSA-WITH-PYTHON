# Write a python program to take a user input
# and print the sum of each digits of the
# number which are less than or equals to
# 5.
# Input:
# N=42765
# Output:
# 11

def sum_of_digit_less_than_5(num):
    sum = 0
    while num>0:
        rem = num%10
        if rem<=5:
            sum+=rem
        num//=10
    print(f"Sum of digit less than 5 is : {sum}")

num = int(input("Enter your number : "))
sum_of_digit_less_than_5(num)