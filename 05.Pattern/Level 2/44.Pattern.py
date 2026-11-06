'''Enter the number of rows : 
5

15 
14 13
12 11 10
9  8  7  6
5  4  3  2  1 '''

def get_pattern(n):
    pattern_size = 1
    num = n*(n+1)//2
    for i in range(1,n+1):
        for j in range(1,pattern_size+1):
            print(f"{num:<3}",end="")
            num-=1

        pattern_size+=1
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)

    