# 1*2+2*3+3*4+4*5+...........upto 100

def getSum(n):
    if n == 1:
        return 1*2

    return (n*(n+1))+getSum(n-1)

num = int(input("Enter your number : "))
res = getSum(num)
print(f"Sum of series is : {res}")