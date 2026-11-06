'''Enter the number of rows:
5

*   * * *
*   *
* * * * *
    *   *
* * *   *  '''

def get_pattern(n):
    mid = n//2+1
    if n%2==0:
        print("Please enter the odd number ")
        return

    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==mid or j==mid or (j==1 and i<mid) or (i==1 and j>mid) or (i==n and j<mid) or (j==n and i>mid):
                print("* ",end="")
            else:
                print("  ",end="")
        print()

num = int(input("Enter the number of rows:"))
get_pattern(num)
