# WAPP to take binary input and print its decimal
# representation.
# i/p: 10100
# o/p: 20

def get_binary_decimal(n):
    decimal = 0
    power = 0
    for i in str(n):
        if i in '23456789':
            print("Please enter the only binary digit")
            return

    while n>0:
        rem = n%10
        decimal = decimal+rem*2**power
        power+=1
        n//=10

    print(f"Binary to decimal is : {decimal}")

binary = int(input("Enter the binary digit : "))
get_binary_decimal(binary)
