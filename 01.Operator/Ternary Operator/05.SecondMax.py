# WAP to find second max of three numbers without using any inbuilt function. 


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a > b and a < c) or (a < b and a > c):
    second_max = a
elif (b > a and b < c) or (b < a and b > c):
    second_max = b
else:
    second_max = c

print(f"The second maximum number is: {second_max}")
