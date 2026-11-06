# WAP to convert a positive number into binary
# form.
# i/p: 20
# o/p: 10100

def decimal_to_binary(num):
    if num<=0:
        print("Please enter the positive number : ")
    else:
        place = 1
        res = 0
        while num>0:
            rem = num%2
            res = res+(rem*place)
            place*=10
            num//=2
        print(f"Decimal to binary is : {res}")


num = int(input("Enter your positive number : "))
decimal_to_binary(num)


