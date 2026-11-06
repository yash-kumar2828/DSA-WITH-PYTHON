'''Enter the number of row :
5
            1
         3  2
      6  5  4
   10 9  8  7
15 14 13 12 11  '''

def get_pattern(n):
    pattern_size = 1
    space = n-1
    
    for i in range(1,n+1):
        num = i*(i+1)//2
        for j in range(1,space+1):
            print(f"{" ":<3}",end="")

        for k in range(1,pattern_size+1):
            print(f"{num:<3}",end="")
            num-=1

        pattern_size+=1
        space-=1
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)