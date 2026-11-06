'''Write a python program to take a user input and return true if all the digits of the number is in decreasing order.
Input:
N=7431
Output:
true'''

def check_decreasing_order(n):
    lastDigit = n%10
    n//=10
    while n>0:
        rem = n%10
        if lastDigit>=rem:
            return False
        lastDigit = rem
        n//=10
    return True

num = int(input("Enter your number : "))
if check_decreasing_order(num):
    print(True)
else:
    print(False)