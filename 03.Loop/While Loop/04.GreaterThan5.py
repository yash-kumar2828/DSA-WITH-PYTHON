# Write a python program to take a user input
# and print each digits of the number which
# are greater than or equals to 5 one by
# one.
# Input:
# N=43705
# Output:
# 5
# 7

def greater_than_five(num):
    while num>0:
        rem = num%10
        if rem>=5:
            print(rem)
        num//=10

num = int(input("Enter your number : "))
greater_than_five(num)