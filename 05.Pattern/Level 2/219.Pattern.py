'''Enter the number of rows :
7

31                30 
29 28          27 26 
25 24 23    22 21 20 
19 18 17 16 15 14 13 
12 11 10    9  8  7  
6  5           4  3  
2                 1    '''


def get_pattern(n):

    left = 1
    right = n
    mid = n//2+1
    num = n*(n+2)//2

    if n%2 == 0:
        print("Please enter the odd number")
        return

    for i in range(1,n+1):

        for j in range(1,n+1):

            if j<=left or j>=right:
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