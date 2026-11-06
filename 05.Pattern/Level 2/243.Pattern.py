'''Enter the number of rows :
7

1  
3  2  
4  5  6  
10 9  8  7  
11 12 13 14 15 
21 20 19 18 17 16 
22 23 24 25 26 27 28  '''

def get_pattern(n):
    start = 1

    for i in range(1,n+1):

        if i%2 != 0:
            for j in range(0,i):
                print(f"{start+j:<3}",end="")

        else:
            for j in range(i-1,-1,-1):
                print(f"{start+j:<3}",end="")

        start+=i
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)





