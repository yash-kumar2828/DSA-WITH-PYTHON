'''Enter the number of rows : 
7

            A  
         B  A  B  
      C  B  A  B  C  
   D  C  B  A  B  C  D  
      C  B  A  B  C  
         B  A  B  
            A      '''


def get_pattern(n):
    pattern_size = 1
    mid = n//2+1
    space = mid

    for i in range(1,n+1):
        for j in range(1,space+1):
            print(f"{' ':<3}",end="")

        col_mid = pattern_size//2+1
        alpha = 64+col_mid
        for k in range(1,pattern_size+1):
            print(f"{chr(alpha):<3}",end="")

            if k < col_mid:
                alpha-=1
            else:
                alpha+=1

        if i<mid:
            pattern_size+=2
            space-=1

        else:
            pattern_size-=2
            space+=1

        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)