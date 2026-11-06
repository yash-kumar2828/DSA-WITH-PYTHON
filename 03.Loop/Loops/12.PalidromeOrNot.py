# WAP to check number is palidrome or not
def isPalidrome(num):
    rev = 0
    temp = num
    while num>0:
        rem = num%10
        rev = rev*10+rem
        num = num//10
    return temp == rev

num = int(input("Enter your number : "))
if isPalidrome(num):
    print(f"{num} is palidrome number")
else:
    print(f"{num} is not palidrome number")
