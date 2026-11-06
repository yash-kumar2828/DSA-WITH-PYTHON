# WAP to get LCM of three number

def getLCM(a,b,c):
    biggest = (a if a>b and a>c else b if b>c else c)
    i = biggest
    while True:
        if i%a==0 and i%b==0 and i%c==0:
            return i
        i = i+biggest


num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))
num3 = int(input("Enter your third number : "))
res = getLCM(num1,num2,num3)
print("The LCM is :",res)