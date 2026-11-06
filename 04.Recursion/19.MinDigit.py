# WAP to find the min digit in the number 

def getMin(n,min):
    if n==0:
        return min

    rem = n%10
    if rem<min:
        min = rem

    return getMin(n//10,min)

num = int(input("Enter your number : "))
min = num%10
res = getMin(num,min)
print(f"Min digit is : {res}")