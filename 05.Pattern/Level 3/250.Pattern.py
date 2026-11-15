'''Enter the number of rows :
5

O  
M  N  
L  K  J  
F  G  H  I  
E  D  C  B  A 

'''


def get_pattern(n):

    alpha = 64+n*(n+1)//2
    pattern_size = 1

    for i in range(1,n+1):

        if i%2 != 0:
            for j in range(0,pattern_size):
                print(f"{chr(alpha-j):<3}",end='')

        else:
            for j in range(pattern_size-1,-1,-1):
                print(f"{chr(alpha-j):<3}",end="")

        pattern_size+=1
        alpha-=i
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)


