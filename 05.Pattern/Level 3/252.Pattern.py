'''Enter the number of rows : 
5

O  
N  G  
M  H  F  
L  I  E  B  
K  J  D  C  A 

'''


def get_pattern(n):

    total = n*(n+1)//2
    pattern_size = 1

    for i in range(1,n+1):
        alpha = 64+total-i+1

        for j in range(0,pattern_size):
            print(f"{chr(alpha):<3}",end="")

            if j%2 == 0:
                alpha = alpha - (2*(n-i)+1)

            else:
                alpha = alpha - (2*(i-j-1))

        pattern_size+=1
        print()


num = int(input("Enter the number of rows : "))
get_pattern(num)