# Find max of three numbers without using any inbuilt function.

a = int(input("Enter your first number : "))
b = int(input("Enter your second number : "))
c = int(input("Enter your third number : "))

res = a if a==b==c and b>c else b if b>c else c

print(f"The max number is : {res}")