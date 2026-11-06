'''Enter the number of rows :
5

            0  
         1  0  2  
      3  4  0  5  6  
   7  8  9  0  10 11 12 
13 14 15 16 0  17 18 19 20   '''

def get_pattern(n):
    pattern_size = 1
    space = n-1
    num = 1

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

        pattern_size+=2
        space-=1
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)
    