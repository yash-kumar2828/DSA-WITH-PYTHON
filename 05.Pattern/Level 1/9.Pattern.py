'''Enter the number of rows:
7
      *
      *
      *
* * * * * * *
      *
      *
      *     '''

def get_pattern(n):
    mid = n//2+1
    if n%2==0:
        print("Please enter the odd number : ")
        return

    for i in range(1,n+1):
        for j in range(1,n+1):
            if mid == i or mid == j:
                print("* ",end="")
            else:
                print("  ",end="")
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)