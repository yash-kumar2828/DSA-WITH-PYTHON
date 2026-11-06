# WAP to check happy number or not

def isHappyNumber(num):
    while num>9:
        sum = 0
        while num>0:
            rem = num%10
            sum = sum+rem**2
            num = num//10
        num = sum
    return num == 1 or num == 7

num = int(input("Enter your number : "))
if isHappyNumber(num):
    print(f"{num} is happy number")
else:
    print(f"{num} is not happy number")

        