'''WAPP to print each digit of a number from right to left
by using recursion.
.n=3472
o/p:
2
7
4
3'''

def print_digit_right_left(n):
    if n==0:
        return
    print(n%10)
    print_digit_right_left(n//10)


num = int(input("Enter your number : "))
res = print_digit_right_left(num)
