# Find max of four numbers without using any inbuilt function.

a = int(input("Enter your first number : "))
b = int(input("Enter your second number : "))
c = int(input("Enter your third number : "))
d = int(input("Enter your fourth number : "))

res = a if a>b and a>c and a>d else b if b>c and b>d else c if c>d else d

print(f"The maximum number is : {res}")

