# Write a python program to take a user input
# and count the even digits of the number.
# Input:
# N=42765
# Output:
# 3

def count_even_digit(num):
    count = 0
    while num>0:
        rem = num%10
        if rem%2==0:
            count+=1
        num//=10
    print(f"The total even digit is {count}")


num = int(input("Enter your number : "))
count_even_digit(num)