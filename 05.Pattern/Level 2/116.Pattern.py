'''Enter the number of rows :
5

1   0   1   0   1   
  1   0   1   0   
    1   0   1   
      1   0   
        1       '''

def get_pattern(n):
    pattern_size = n
    space = 0

    for i in range(1,n+1):
        for j in range(1,space+1):
            print(f"{' ':<2}",end="")

        for k in range(1,pattern_size+1):
            print(f"{k%2:<4}",end="")

        pattern_size-=1
        space+=1
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)
