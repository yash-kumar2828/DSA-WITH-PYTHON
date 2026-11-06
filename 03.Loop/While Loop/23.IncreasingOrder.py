'''Write a python program to take a user input and return true if all the digits of the number is in increasing order.
Input:
N=5689
Output:
true'''

def check_increasing_order(n):
    lastDigit = n%10
    n//=10
    while n>0:
        rem = n%10
        if lastDigit<=rem:
            return False
        lastDigit = rem
        n//=10
    return True

num = int(input("Enter your number : "))
if check_increasing_order(num):
    print(True)
else:
    print(False)
