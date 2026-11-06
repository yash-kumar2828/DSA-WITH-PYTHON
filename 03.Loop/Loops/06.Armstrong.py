# WAP to check armstrong or not 

def countDigit(num):
    count = 0
    while num>0:
        count = count+1
        num = num//10
    return count

def isArmstrong(num):
    res = 0
    temp = num
    digit = countDigit(num)
    while num>0:
        rem = num%10
        res = res+rem**digit
        num = num//10
    return temp == res

num = int(input("Enter your number : "))
if isArmstrong(num):
    print(f"{num} is armstrong number")
else:
    print(f"{num} is not armstrong number")
