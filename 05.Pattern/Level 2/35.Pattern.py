'''Enter the row : 
7
*                       *
* *                   * *
* * *               * * *
* * * *           * * * *
* * * * *       * * * * *
* * * * * *   * * * * * *
* * * * * * * * * * * * *  '''

def get_pattern(n):
    pattrn_size = 2*n-1
    left_star = 1
    right_star = pattrn_size


    for i in range(1,n+1):
        for j in range(1,pattrn_size+1):
            if j<=left_star or j>=right_star:
                print("* ",end="")
            else:
                print("  ",end="")

        left_star+=1
        right_star-=1
        print()

num = int(input("Enter the row : "))
get_pattern(num)
