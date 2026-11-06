'''Enter the number of rows :
7

A                 A  
B  B           B  B  
C  C  C     C  C  C  
D  D  D  D  D  D  D  
E  E  E     E  E  E  
F  F           F  F  
G                 G    '''


def get_pattern(n):
    left = 1
    right = n
    mid = n//2+1

    if n%2 == 0:
        print("Please enter the odd number ")
        return

    for i in range(1,n+1):
        alpha = 64
        for j in range(1,n+1):
            if j<=left or j>=right:
                print(f"{chr(alpha+i):<3}",end="")

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