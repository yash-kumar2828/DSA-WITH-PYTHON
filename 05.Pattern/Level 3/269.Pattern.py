'''Enter the number of rows :
7

         *  @  @  @  @                 @  @  @  @  *  
      *  *           @                 @           *  *  
   *  *  *           @                 @           *  *  *  
*  *  *  *           @                 @           *  *  *  *  
   *  *  *              *  *  *  *  *              *  *  *  
      *  *              *  *  *  *  *              *  *  
         *              *  *  *  *  *              * 
         
'''


def get_pattern(n):

    mid = n//2+1
    start_space = n//2
    end_star = 5*n//2+1

    if n%2 == 0:
        print("Please enter the odd number ")
        return
    
    for i in range(1,n+1):
        # First Section 
        for j in range(1,mid+1):
            if j<=start_space:
                print(f"{' ':<3}",end="")
            else:
                print(f"{'*':<3}",end="")

        # Second section
        for j in range(mid+1,n+2):
            if i == 1 or (j == n+1 and i<=mid):
                print(f"{'@':<3}",end="")
            else:
                print(f"{' ':<3}",end="")

        # Third section
        for j in range(n+2,2*n):
            if i>mid:
                print(f"{'*':<3}",end='')
            else:
                print(f"{' ':<3}",end="")

        # Fourth Section
        for j in range(2*n,5*n//2+1):
            if i == 1 or (j == 2*n and i<=mid):
                print(f"{'@':<3}",end="")
            else:
                print(f"{' ':<3}",end='')

        # Fifth Section
        for j in range(5*n//2+1,end_star+1):
            print(f"{'*':<3}",end='')


        if i<mid:
            start_space-=1
            end_star+=1
        else:
            start_space+=1
            end_star-=1

        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)