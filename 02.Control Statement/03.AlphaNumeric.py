# WAP to check whether the given character is alphanumeric character or a special character.

# Method-1 
ch = input("Enter your character : ")

if 'a'<=ch<='z' or 'A'<=ch<='Z' or '0'<=ch<="9":
    print(f"{ch} is alphanumeric")

else:
    print(f"{ch} is special character") 


# Method-2
ch2 = input("Enter your character : ")

if ch2.isalnum():
    print(f"{ch2} is alphanumeric")

else:
    print(f"{ch2} is special character")