# WAPP to take two user inputs and print HCF of the two numbers.

def getHCF(a,b):
    if a==0:
        return b

    return getHCF(b%a,a)

num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))
res = getHCF(num1,num2)
print("HCF of number is : ",res)