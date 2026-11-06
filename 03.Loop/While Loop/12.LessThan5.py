# Write a python program to take a user input
# and count all the digits of the number
# which are less than or equals to 5.
# Input:
# N=42765
# Output:
# 3

def less_than_five(num):
    count = 0
    while num>0:
        rem = num%10
        if rem<=5:
            count+=1
        num//=10
    print(f"Total digit is : {count}")

num = int(input("Enter your number : "))
less_than_five(num)