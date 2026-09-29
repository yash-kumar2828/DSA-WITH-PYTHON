# Check no is Even or odd 

num = int(input("Enter your number : "))

res = f"{num} is even number" if num & 1 == 0 else f"{num} is odd number"
print(res)