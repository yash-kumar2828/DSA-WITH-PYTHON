'''Enter the number of rows :
5

A  
B  I  
C  H  J  
D  G  K  N  
E  F  L  M  O 

'''

def get_pattern(n):
    patter_size = 1

    for i in range(1,n+1):
        alpha = 64+i

        diff1 = 2 * (n-i)+1
        diff2 = 2 * (i-1)

        for j in range(1,patter_size+1):
            print(f"{chr(alpha):<3}",end='')

            if j%2 != 0:
                alpha+=diff1
            else:
                alpha+=diff2
            diff2-=2

        patter_size+=1
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)