'''Enter the number of rows :
7    
            1
          1 2
        1 2 3
      1 2 3 4
    1 2 3 4 5
  1 2 3 4 5 6
1 2 3 4 5 6 7  '''

def get_pattern(n):
    pattern_size = 1
    space = n-1

    for i in range(1,n+1):
        for j in range(1,space+1):
            print(f"{" ":<3}",end="")

        for k in range(1,pattern_size+1):
            print(f"{k:<3}",end="")

        pattern_size+=1
        space-=1
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)