'''Enter the number of rows : 
5

11  
12  10  
13  9   4   
14  8   5   3   
15  7   6   2   1 
'''

def get_pattern(n):

    patternSize = 1
    total = n*(n+1)//2

    for i in range(1,n+1):
        num = total-n+i

        for j in range(0,patternSize):
            print(f"{num:<4}",end="")

            if j%2 == 0:
                num = num-2*(i-j-1)
            else:
                num = num-(2*(n-i)+1)

        patternSize+=1
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)