'''Enter the number of rows : 
7

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
1 2 3 4 5 6 7  '''
def get_pattern(n):
    pattern_size = 1
    for i in range(1,n+1):
        for j in range(1,pattern_size+1):
            print(f"{j:<2}",end="")

        pattern_size+=1
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)