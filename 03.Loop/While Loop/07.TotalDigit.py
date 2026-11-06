# Write a python program to take a user input
# and count the total digit of the number.
# Input:
# N=43705
# Output:
# 5

def countDigit(num):
    count = 0
    while num>0:
        count+=1
        num//=10
    print(count)

num = int(input("Enter your number : "))
countDigit(num)
