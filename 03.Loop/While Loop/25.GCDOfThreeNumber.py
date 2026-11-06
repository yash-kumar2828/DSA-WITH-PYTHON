# WAP to get GCD/HCF of three number

def getHCF(a,b,c):
    small = (a if a<b and a<c else b if b<c else c)
    i = small
    while True:
        if a%i==0 and b%i==0 and c%i==0:
            return i
        i=i-1

num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))
num3 = int(input("Enter your third number : "))

res = getHCF(num1,num2,num3)
print(f"HCF of three number is : {res}")