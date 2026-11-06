'''Enter the number of rows :
5

A  A  A  A  A  A  A  A  A  
   B  B  B  B  B  B  B  
      C  C  C  C  C  
         D  D  D  
            E     '''


def get_pattern(n):
    pattern_size = 2*n-1
    space = 0
    alpha = 64

    for i in range(1,n+1):
        for j in range(1,space+1):
            print(f"{' ':<3}",end='')

        for k in range(1,pattern_size+1):
            print(f"{chr(alpha+i):<3}",end="")

        pattern_size-=2
        space+=1
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)