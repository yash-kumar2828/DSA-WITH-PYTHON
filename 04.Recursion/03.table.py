# WAPP to generate table of a number by using recursion.

def print_table(n,i):
    if i>10:
        return
    print(f"{n}*{i}={n*i}")
    print_table(n,i+1)

num = int(input("Enter your number : "))
print_table(num,1)
