'''Enter the number of rows : 
5
        A   
      A   B   
    A   B   C   
  A   B   C   D   
A   B   C   D   E  '''


def get_pattern(n):
    pattern_size = 1
    space = n-1
    alpha = 64

    for i in range(1,n+1):
        for j in range(1,space+1):
            print(f"{' ':<2}",end="")

        for k in range(1,pattern_size+1):
            print(f"{chr(alpha+k):<4}",end="")

        pattern_size+=1
        space-=1
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)
