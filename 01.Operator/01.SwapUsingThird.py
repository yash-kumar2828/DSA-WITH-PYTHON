# WAP to swap two numbers using a third variable.

num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))

print(f"num1 = {num1} & num2 = {num2}")

temp = num1
num1 = num2
num2 = temp

print(f"num1 = {num1} & num2 = {num2}")
