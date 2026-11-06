# Write a python program to take a user input and reverse
# the number.
# Input:
# N=3745
# Output:
# 5473

def reverseNumber(num):
    rev = 0
    while num>0:
        rem = num%10
        rev = rev*10+rem
        num//=10
    print(f"The reverse number is : {rev}")

num = int(input("Enter your number : "))
reverseNumber(num)