'''Enter the number of rows :
5

O   N   M   L   K   
  J   I   H   G   
    F   E   D   
      C   B   
        A       '''


def get_pattern(n):

    pattern_size = n
    space = 0
    alpha = 64+n*(n+1)//2

    for i in range(1,n+1):
        for j in range(1,space+1):
            print(f"{' ':<2}",end="")

        for k in range(1,pattern_size+1):
            print(f"{chr(alpha):<4}",end="")
            alpha-=1

        pattern_size-=1
        space+=1
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)