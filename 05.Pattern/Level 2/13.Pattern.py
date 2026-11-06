'''Enter the number of rows:
7
* * * * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
*        '''


def get_pattern(n):
    pattern_size = n
    for i in range(1,n+1):
        for j in range(1,pattern_size+1):
            print("* ",end="")

        pattern_size-=1
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)