'''Enter the number of rows : 
7

1 
2 1
3 2 1 
4 3 2 1 
5 4 3 2 1
6 5 4 3 2 1
7 6 5 4 3 2 1  '''

def get_pattern(n):
    pattern_size = 1
    for i in range(1,n+1):
        num = i
        for j in range(1,pattern_size+1):
            print(f"{num:<3}",end="")
            num-=1

        pattern_size+=1
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)