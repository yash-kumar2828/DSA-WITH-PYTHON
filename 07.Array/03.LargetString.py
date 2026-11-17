# For the given array of Strings, print the largest string.

def get_largest_string(s):
    largest_str = s[0]

    for i in range(len(s)):
        if s[i]>largest_str:
            largest_str = s[i]

    print(f"Largest string is : {largest_str}")


s = ["Yash Kumar","I am happy","You are so beautiful","I am yash kumar"]
get_largest_string(s)