# WAP to check the no. is strong or not

def factorial(num):
    fact = 1
    if num == 1 or num == 2:
        return num
    else:
        for i in range(1,num+1):
            fact = fact*i
        return fact

def isStrong(num):
    res = 0
    temp = num
    while num>0:
        rem = num%10
        res = res+factorial(rem)
        num = num//10
    return temp == res


num = int(input("Enter your number : "))
if isStrong(num):
    print(f"{num} is strong number")
else:
    print(f"{num} is not strong number")


