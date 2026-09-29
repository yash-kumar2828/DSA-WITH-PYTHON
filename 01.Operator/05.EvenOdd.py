# WAP to check even or odd without modulus(%).

num = int(input("Enter your number : "))

if num & 1==0:
    print(f"{num} is even number")

else:
    print(f"{num} is odd number") 