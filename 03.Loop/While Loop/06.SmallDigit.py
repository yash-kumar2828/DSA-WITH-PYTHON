# Write a java program to take a user input
# and print the difference of biggest digit
# and smallest digit of the number.
# Input:
# N=42375
# Output:
# 5

def subtract_largest_small_digit(num):
    small = 9
    largest = 0
    while num>0:
        rem = num%10
        if rem<small:
            small = rem
        elif rem>largest:
            largest = rem
        num//=10
    print(largest-small)

num = int(input("Enter your number : "))
subtract_largest_small_digit(num)
