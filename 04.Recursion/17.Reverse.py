# WAPP to reverse the number using recursion 

def getReverse(n,rev=0):
    if n==0:
        return rev
    rem = n%10
    rev = rev*10+rem
    return getReverse(n//10,rev)

num = int(input("Enter your number : "))
res = getReverse(num)
print(f"The reverse number is : {res}")
