# WAPP to calculate power by using recursion.

def getPower(base,exponent):
    if exponent == 0:
        return 1

    return base*getPower(base,exponent-1)

base = int(input("Enter your base : "))
exponent = int(input("Enter your exponent : "))
res = getPower(base,exponent)
print(f"{base} to the power {exponent} is : {res}")

    