'''Enter the number of rows :
5

25 16 15 6  5  
24 17 14 7  4  
23 18 13 8  3  
22 19 12 9  2  
21 20 11 10 1   '''

def get_pattern(n):

    for i in range(1,n+1):

        for j in range(n):

            if j%2 == 0:
                val = n*(n-j) - i + 1

            else:
                val = n**2 - ((j+1) * n-i+1) + 1

            print(f"{val:<3}",end="")

        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)