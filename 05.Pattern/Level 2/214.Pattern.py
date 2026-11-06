'''Enter the number of rows :
7

1                 7  
1  2           6  7  
1  2  3     5  6  7  
1  2  3  4  5  6  7  
1  2  3     5  6  7  
1  2           6  7  
1                 7    '''


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
                print(f"{j:<3}",end="")

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
