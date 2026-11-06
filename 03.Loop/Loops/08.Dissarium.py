# WAP to check dissarium number or not 

def countDigit(num):
    count = 0
    while num>0:
        count+=1
        num//=10
    return count


def isDissarium(num):
    res = 0
    temp = num
    count = countDigit(num)
    while num>0:
        rem = num%10
        res = res+rem**count
        count = count-1
        num = num//10

    return temp == res

num = int(input("Enter your number : "))

if isDissarium(num):
    print(f"{num} is dissarium number")
else:
    print(f"{num} is not dissarium number")