'''Enter the number of rows :
5
            A  
         B  B  B  
      C  C  C  C  C  
   D  D  D  D  D  D  D  
E  E  E  E  E  E  E  E  E  '''


def get_pattern(n):
    pattern_size = 1
    space = n-1

    for i in range(1,n+1):
        alpha = 64+i
        for j in range(1,space+1):
            print(f"{' ':<3}",end="")

        for k in range(1,pattern_size+1):
            print(f"{chr(alpha):<3}",end="")

        pattern_size+=2
        space-=1
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)