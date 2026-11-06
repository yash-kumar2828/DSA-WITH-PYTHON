'''Enter the number of rows :
5

A   A   A   A   A   
  B   B   B   B   
    C   C   C   
      D   D   
        E    '''


def get_pattern(n):

    pattern_size = n
    space = 0

    for i in range(1,n+1):
        alpha = 64+i
        for j in range(1,space+1):
            print(f"{' ':<2}",end="")

        for k in range(1,pattern_size+1):
            print(f"{chr(alpha):<4}",end="")

        pattern_size-=1
        space+=1
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)