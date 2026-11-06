'''Enter the number of rows :
5

I  H  G  F  E  D  C  B  A  
   G  F  E  D  C  B  A  
      E  D  C  B  A  
         C  B  A  
            A         '''


def get_pattern(n):
    pattern_size = 2*n-1
    space = 0
    

    for i in range(1,n+1):
        for j in range(1,space+1):
            print(f"{' ':<3}",end='')

        alpha = 64 + pattern_size

        for k in range(1,pattern_size+1):
            print(f"{chr(alpha):<3}",end="")
            alpha-=1

        pattern_size-=2
        space+=1
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)