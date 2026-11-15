'''Enter the number of rows :
7

1   
2   13  
3   12  14  
4   11  15  22  
5   10  16  21  23  
6   9   17  20  24  27  
7   8   18  19  25  26  28 '''


def get_pattern(n):
    patternSize = 1

    for i in range(1,n+1):
        num = i

        diff1 = 2*(n-i)+1
        diff2 = 2*(i-1)
        for j in range(1,patternSize+1):
            print(f"{num:<4}",end="")

            if j%2!=0:
                num+=diff1
            else:
                num+=diff2
            diff2-=2

        patternSize+=1
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)