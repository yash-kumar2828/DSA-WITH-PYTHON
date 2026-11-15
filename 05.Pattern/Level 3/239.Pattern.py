'''Enter the number of rows :
5

1  2  3  4  5 
10 9  8  7  6
11 12 13 14 15
20 19 18 17 16
21 22 23 24 25  '''



def get_pattern(n):

    for i in range(n):
        start = i * n + 1 

        if i%2 == 0:
            for j in range(start,start+n):
                print(f"{j:<4}",end="")

        else:
            for j in range(start+n-1,start-1,-1):
                print(f"{j:<4}",end="")

        print()



num = int(input("Enter the number of rows : "))
get_pattern(num)
