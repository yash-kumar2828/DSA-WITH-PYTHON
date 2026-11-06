# WAPP to generate numbers from 1 to 10 by using recursion.

def print_1_to_n(n):
    if n==0:
        return
    print_1_to_n(n-1)
    print(n,end=" ")

num = int(input("Enter your number : "))
print_1_to_n(num)