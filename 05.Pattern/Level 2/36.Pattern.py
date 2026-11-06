'''Enter the row :
7
*           *
*           *
*           *
*           *
* *       * *
* * *   * * *
* * * * * * *  '''

def get_pattern(n):
    mid = n//2+1
    left_star = 1
    right_star = n

    if n%2==0:
        print("Please enter the odd number")
        return

    for i in range(1,n+1):
        for j in range(1,n+1):
            if j<=left_star or j>=right_star:
                print("* ",end="")
            else:
                print("  ",end="")

        if i>=mid:
            left_star+=1
            right_star-=1
        print()

num = int(input("Enter the row : "))
get_pattern(num)