# Write a python program to take a user input
# and count how many 3 has appeared in
# the number
# Input:
# N=4373533
# Output:
# 4

def countAppeared(num):
    count = 0
    while num>0:
        rem = num%10
        if rem == 3:
            count+=1
        num//=10
    print(count)

num = int(input("Enter your number : "))
countAppeared(num)