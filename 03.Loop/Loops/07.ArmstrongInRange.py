# WAP to print and count armstrong number 

def countDigit(num):
    count = 0
    while num>0:
        count+=1
        num//=10
    return count


def isArmstrong(num):
    digit = countDigit(num)
    res = 0
    temp = num
    while num>0:
        rem = num%10
        res += rem**digit
        num//=10
    return temp == res

def armstrongInRange(start,end):
    count = 0
    for i in range(start,end+1):
        if isArmstrong(i):
            print(i,end=" ")
            count = count+1
    print(f"\nThe total armstrong number is : {count}") 

start = int(input("Enter starting value : "))
end = int(input("Enter ending value : "))
armstrongInRange(start,end)
    