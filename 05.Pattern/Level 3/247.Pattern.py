'''Enter the number of rows : 
7

28  
27  16  
26  17  15  
25  18  14  7   
24  19  13  8   6   
23  20  12  9   5   2   
22  21  11  10  4   3   1
'''


def get_pattern(n):

    total = n*(n+1)//2
    patternSize = 1

    for i in range(1,n+1):
        num = total-i+1

        for j in range(0,patternSize):
            print(f"{num:<4}",end="")

            if j%2 == 0:
                num = num - (2*(n-i)+1)
            else:
                num = num - (2*(i-j-1))

        patternSize+=1
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)