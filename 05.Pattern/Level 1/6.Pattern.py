'''Enter the number of rows:
9
* * * * * * * * *
* * * * * * * * *
* *           * *
* *           * *
* *           * *
* *           * *
* *           * *
* * * * * * * * *
* * * * * * * * *   '''

def get_pattern(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==1 or j==1 or i==n or j==n or i==2 or j==2 or i==n-1 or j==n-1:
                print("* ",end="")
            else:
                print("  ",end="")
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)

