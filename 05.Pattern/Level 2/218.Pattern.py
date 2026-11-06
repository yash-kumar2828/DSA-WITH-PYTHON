'''Enter the number of rows :
7

1                 2  
3  4           5  6  
7  8  9     10 11 12 
13 14 15 16 17 18 19 
20 21 22    23 24 25 
26 27          28 29 
30                31   '''


def get_pattern(n):
    left = 1
    right = n
    num = 1
    mid = n//2+1

    if n%2 == 0:
        print("Please enter the odd number")
        return

    for i in range(1,n+1):
        for j in range(1,n+1):

            if j<=left or j>=right:
                print(f"{num:<3}",end="")
                num+=1

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
        