'''Enter the number of rows :
7

1                 1  
2  2           2  2  
3  3  3     3  3  3  
4  4  4  4  4  4  4  
5  5  5     5  5  5  
6  6           6  6  
7                 7     '''


def get_pattern(n):
    left = 1
    right = n
    mid = n//2+1

    if n%2 == 0:
        print("Please enter the odd number ")
        return

    for i in range(1,n+1):

        for j in range(1,n+1):
            if j<=left or j>=right:
                print(f"{i:<3}",end="")
            else:
                print(f"{' ':<3}",end="")

        if i<mid:
            left+=1
            right-=1
        else:
            left-=1
            right+=1

        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)
