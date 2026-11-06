# Write a python program to take a user input
# and count how many 0 digit is in number.
# Input:
# N=430705
# Output:
# 2

def countZero(num):
    count = 0
    while num>0:
        rem = num%10
        if rem == 0:
            count =count+1
        num = num//10
    print(count)

num = int(input("Enter yor number : "))
countZero(num)