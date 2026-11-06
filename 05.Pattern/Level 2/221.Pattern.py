'''Enter the number of rows :
7

A                 G  
A  B           F  G  
A  B  C     E  F  G  
A  B  C  D  E  F  G  
A  B  C     E  F  G  
A  B           F  G  
A                 G   '''


def get_pattern(n):
    left = 1
    right = n
    mid = n//2+1

    if n%2 == 0:
        print("Please enter the odd number")
        return

    for i in range(1,n+1):

        alpha = 65

        for j in range(1,n+1):

            if j<=left or j>=right:
                print(f"{chr(alpha):<3}",end="")
            else:
                print(f"{' ':<3}",end="")

            alpha+=1

        if i<mid:
            left+=1
            right-=1
        else:
            left-=1
            right+=1

        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)