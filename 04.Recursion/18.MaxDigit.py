# WAP to find the max digit in the number 

def getMax(n,max):
    if n==0:
        return max
    rem = n%10
    if rem>max:
        max = rem
    return getMax(n//10,max)


num = int(input("Enter your number : "))
max = num%10
res = getMax(num,max)
print(f'max digit is : {res}')