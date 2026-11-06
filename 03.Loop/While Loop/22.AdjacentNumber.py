'''Write a python program to take a user input and
return true if any two adjacent numbers are
not same.
Input:
N=4207065
Output:
true'''

def check_adjacent(n):
    lastDigit=n%10
    n//=10
    while n>0:
        rem = n%10
        if rem == lastDigit:
            return False

        lastDigit=rem
        n//=10
    return True

num = int(input("Enter your number : "))
 
if check_adjacent(num):
    print(True)
else:
    print(False)