# WAP to take three inputs and print all are equal if all have same value or print biggest value of three numbers using if else statement.

num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))
num3 = int(input("Enter your third number : "))

if num1==num2==num3:
    print("All value are equal")

elif num1>num2 and num1>num3:
    print(f"{num1} is greatest number")

elif num2>num3:
    print(f"{num2} is greatest number")

else:
    print(f"{num3} is greatest number")