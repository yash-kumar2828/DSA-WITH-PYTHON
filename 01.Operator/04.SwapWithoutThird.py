# WAP to swap two numbers without using a third variable or without using +, –, * or / operator. 

num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))

print(f"num1 = {num1} & num2 = {num2}")

num1 = num1^num2
num2 = num1^num2
num1 = num1^num2

print(f"num1 = {num1} & num2 = {num2}")