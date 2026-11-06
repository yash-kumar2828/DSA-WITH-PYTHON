'''Enter the number of rows :
7

3  2  1  0  1  2  3  
   2  1  0  1  2  
      1  0  1  
         0  
      1  0  1  
   2  1  0  1  2  
3  2  1  0  1  2  3    '''


def get_pattern(n):
    pattern_size = n
    mid = n//2+1
    space = 0

    if n%2 == 0:
        print("Please enter the odd number ")
        return

    for i in range(1,n+1):
        for j in range(1,space+1):
            print(f"{' ':<3}",end="")

        col_mid = pattern_size//2+1
        num = mid-space-1

        for k in range(1,pattern_size+1):
            print(f"{num:<3}",end="")

            if k < col_mid:
                num-=1
            else:
                num+=1

        if i<mid:
            pattern_size-=2
            space+=1
            

        else:
            pattern_size+=2
            space-=1

        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)

