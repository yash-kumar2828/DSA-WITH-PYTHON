'''Enter the number of rows:
7
*           *
  *       *
    *   *
      *
    *   *
  *       *
*           *  '''

def get_pattern(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j or i+j==n+1:
                print("* ",end="")
            else:
                print("  ",end="")
        print()

num = int(input("Enter the number of rows:"))
get_pattern(num)

    