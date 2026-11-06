# WAPP to get digit sum of a number by using recursion.

def sum_of_digit(n):
    if n<=9:
        return n
    return ((n%10)+sum_of_digit(n//10))

num = int(input("Enter your number : "))
res = sum_of_digit(num)
print(f"Sum of digit is : {res}")