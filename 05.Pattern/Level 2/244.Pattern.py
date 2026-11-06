'''Enter the number of rows : 
7

28 
26 27 
25 24 23 
19 20 21 22 
18 17 16 15 14 
8  9  10 11 12 13 
7  6  5  4  3  2  1   '''


def get_pattern(n):

    start = 0
    for i in range(1,n+1):
        start+=i
    
    for i in range(1,n+1):
        if i%2 != 0:
            for j in range(0,i):
                print(f"{start-j:<3}",end="")

        else:
            for j in range(i-1,-1,-1):
                print(f"{start-j:<3}",end="")

        start = start-i
        print()


    
num = int(input("Enter the number of rows : "))
get_pattern(num)