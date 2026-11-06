'''Enter the number of rows : 
5
        1   
      2   3   
    4   5   6   
  7   8   9   10  
11  12  13  14  15 '''


def get_pattern(n):
    pattern_size = 1
    space = n-1
    num = 1

    for i in range(1,n+1):
        for j in range(1,space+1):
            print(f"{' ':<2}",end="")

        for k in range(1,pattern_size+1):
            print(f"{num:<4}",end="")
            num+=1

        pattern_size+=1
        space-=1
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)