# WAP to swap two numbers without using a third variable. 

# Method-1
num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))

print(f"num1 = {num1} & num2 = {num2}")

num1,num2 = num2,num1

print(f"num1 = {num1} & num2 = {num2}")


# Method-2
a = int(input("Enter your first number : "))
b = int(input("Enter your second number : "))
print(f"a = {a} & b = {b}")

a = a+b
b = a-b
a = a-b

print(f"a = {a} & b = {b}")




