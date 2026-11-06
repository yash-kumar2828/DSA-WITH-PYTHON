# WAP to print and count strong number in given range

def factorial(num):
    fact = 1
    if num == 1 or num == 1:
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
        res = res + factorial(rem)
        num = num//10
    return temp == res

def strongInRange(start,end):
    count = 0
    for i in range(start,end):
        if isStrong(i):
            print(i,end=" ")
            count = count+1

    print(f"\nThe total strong number is : {count}")


start = int(input("Enter starting value : "))
end = int(input("Enter ending value : "))
strongInRange(start,end)

