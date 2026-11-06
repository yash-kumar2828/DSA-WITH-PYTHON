'''Enter the number of rows :
5
        5   
      5   4   
    5   4   3   
  5   4   3   2   
5   4   3   2   1  '''

def get_pattern(n):
    pattern_size = 1
    space = n-1

    for i in range(1,n+1):
        num = n
        for j in range(1,space+1):
            print(f"{' ':<2}",end="")

        for k in range(1,pattern_size+1):
            print(f"{num:<4}",end="")
            num-=1

        pattern_size+=1
        space-=1
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)