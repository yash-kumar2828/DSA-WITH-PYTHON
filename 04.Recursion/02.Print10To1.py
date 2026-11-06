# WAPP to generate numbers from 10 to 1 by using recursion.

def print_n_to_1(n):
    if n==0:
        return
    print(n,end=" ")
    print_n_to_1(n-1)

num = int(input("Enter your number : "))
print_n_to_1(num)