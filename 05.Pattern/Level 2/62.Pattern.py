'''Enter the number of rows :
5
            15 
         13 14 
      10 11 12 
   6  7  8  9  
1  2  3  4  5  '''

def get_pattern(n):
    pattern_size = 1
    space = n-1

    

    for i in range(1,n+1):
        num = (n*(n+1)//2)-(i*(i+1)//2)+1
        for j in range(1,space+1):
            print(f"{" ":<3}",end="")

        for k in range(1,pattern_size+1):
            print(f"{num:<3}",end="")
            num+=1

        pattern_size+=1
        space-=1
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)