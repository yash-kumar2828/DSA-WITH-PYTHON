# WAPP to get digit count of a number by using recursion.

def count_digit(n):
    if n<0:
        n=abs(n)
    if n<=9:
        return 1
    return 1+count_digit(n//10)

num = int(input("Enter your number : "))
res = count_digit(num)
print(f"The no. of digit is : {res}")

