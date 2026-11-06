'''Enter the number of rows :
5
            1  
         1  2  1  
      1  2  3  2  1  
   1  2  3  4  3  2  1  
1  2  3  4  5  4  3  2  1  '''

def get_pattern(n):
    pattern_size = 1
    space = n-1

    for i in range(1,n+1):
        num = 1
        for j in range(1,space+1):
            print(f"{' ':<3}",end="")

        
        col_mid = pattern_size//2+1
        for k in range(1,pattern_size+1):
            print(f"{num:<3}",end="")
            if k<col_mid:
                num+=1
            else:
                num-=1

        pattern_size+=2
        space-=1
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)
