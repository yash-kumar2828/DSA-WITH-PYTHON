'''Enter the number of rows :
7

1                 1  
1  2           2  1  
1  2  3     3  2  1  
1  2  3  4  5  4  3  
1  2  3     3  2  1  
1  2           2  1  
1                 1    '''


def get_pattern(n):

    left = 1
    right = n
    mid = n//2+1

    if n%2 == 0:
        print("Please enter the odd number ")
        return

    for i in range(1,n+1):

        num = 1

        for j in range(1,n+1):

            if j<=left:
                print(f"{num:<3}",end="")
                num+=1

            elif j>=right:
                if j == right:
                    num = n-j+1
                print(f"{num:<3}",end="")
                num-=1


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
