'''Enter the number of rows :
7

1
1 0
1 0 1
1 0 1 0
1 0 1 0 1
1 0 1 0 1 0
1 0 1 0 1 0 1   '''

def get_pattern(n):
    pattern_size = 1

    for i in range(1,n+1):
        for j in range(1,pattern_size+1):
            print(f"{j%2:<2}",end="")

        pattern_size+=1
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)

