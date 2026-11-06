'''Enter the number of rows :
7

25 24 23 22 21 
16 17 18 19 20 
15 14 13 12 11 
6  7  8  9  10 
5  4  3  2  1   '''


def get_pattern(n):

    for i in range(n):
        start = n*(n-i)

        if i%2 == 0:
            for j in range(start , start-n , -1):
                print(f"{j:<3}",end="")

        else:
            for j in range(start-n+1 , start+1):
                print(f"{j:<3}",end="")


        print()


num = int(input("Enter the number of rows : "))
get_pattern(num)
