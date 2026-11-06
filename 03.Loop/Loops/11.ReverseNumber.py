# WAP to reverse the number 

def reverseNumber(num):
    rev = 0
    while num>0:
        rem = num%10
        rev = rev*10+rem
        num = num//10
    return rev

num = int(input("Enter your number : "))
print(f"The reverse number is : {reverseNumber(num)}")