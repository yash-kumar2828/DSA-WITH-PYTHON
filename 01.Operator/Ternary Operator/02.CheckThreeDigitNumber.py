# Check Three digit number 

num = int(input("Enter your number : "))

res = f"{num} is three digit number" if num>=100 and num<=999 else f"{num} is not three digit number"

print(res)