# Write a python program to take a String input and
# check whether the given String is a palindrome
# String or not.
# Palindrome String: if String is same from both side
# Input:
# String s1=“madam”
# Output:
# madam is a Palindrome String

def check_paridrome(s):
    i = 0
    rev = ""
    while i<len(s):
        rev = rev+s[-1-i]
        i+=1
    return s==rev


s = input("Enter your string : ")
if check_paridrome(s):
    print(f"{s} is palidrome string")
else:
    print(f"{s} is not a palidrome string")