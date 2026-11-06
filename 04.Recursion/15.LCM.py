# WAPP to take three user inputs and print LCM of the two numbers.

def getHCF(a,b):
    if a==0:
        return b
    return getHCF(b%a,a)

def getLCM(n1,n2):
    hcf = getHCF(n1,n2)
    return (n1*n2)//hcf


num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))
res = getLCM(num1,num2)
print(res)