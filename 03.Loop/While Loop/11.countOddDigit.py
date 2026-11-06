# Write a python program to take a user input
# and count the odd digits of the number.
# Input:
# N=42765
# Output:
# 2

def count_odd_digit(num):
    count = 0
    while num>0:
        rem = num%10
        if rem%2 == 1:
            count+=1
        num//=10
    print(f"The total odd digit is : ")

num = int(input("Enter your number : "))
count_odd_digit(num)