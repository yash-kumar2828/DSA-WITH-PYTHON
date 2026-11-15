'''Enter the number of rows :
5

5   
4   6   
3   7   12  
2   8   11  13  
1   9   10  14  15 

'''


def get_pattern(n):
    patternSize = 1


    for i in range(1,n+1):
        num = n-i+1

        for j in range(0,patternSize):
            print(f"{num:<4}",end="")

            if j%2==0:
                num = num + 2*(i-j-1)
            else:
                num = num+2*(n-i)+1

        patternSize+=1
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)