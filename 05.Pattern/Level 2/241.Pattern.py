'''Enter the number of rows :
5

1  10 11 20 21 
2  9  12 19 22 
3  8  13 18 23 
4  7  14 17 24 
5  6  15 16 25   '''


def get_pattern(n):

    for i in range(1,n+1):

        for j in range(n):

            if j%2 == 0:
                val = (j*n) + i

            else:
                val = (j+1)*n - i + 1

            print(f"{val:<3}",end="")

        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)