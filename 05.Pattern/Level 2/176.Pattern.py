'''Enter the number of rows :
7

            0  
         1  0  2  
      3  4  0  5  6  
   7  8  9  0  10 11 12 
      13 14 0  15 16 
         17 0  18 
            0     '''


def get_pattern(n):
    pattern_size = 1
    mid = n//2+1
    space = mid
    num = 1
    
    if n%2==0:
        print("Please enter the odd number ")
        return 
    
    for i in range(1,n+1):
        for j in range(1,space+1):
            print(f"{' ':<3}",end="")

        col_mid = pattern_size//2+1

        for k in range(1,pattern_size+1):
            if k == col_mid:
                print(f"{0:<3}",end="")
            else:
                print(f"{num:<3}",end="")
                num+=1

        if i<mid:
            pattern_size+=2
            space-=1
        else:
            pattern_size-=2
            space+=1
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)