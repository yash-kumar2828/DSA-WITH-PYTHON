'''WAPP to print each digit of a number from left to right
by using recursion.
.n=3472
o/p:
3
4
7
2'''

def print_digit_left_to_right(n):
    if n==0:
        return
    print_digit_left_to_right(n//10)
    print(n%10)

num = int(input("Enter your number : "))
print_digit_left_to_right(num)