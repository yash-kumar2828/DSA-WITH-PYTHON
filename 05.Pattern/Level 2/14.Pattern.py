'''Enter the row:
7
* 
* *
* * *
* * * *
* * *
* * 
*     '''

def get_pattern(n):
    pattern_size = 1
    mid = n//2+1
    if n%2==0:
        print("Please enter the odd number ")
        return
    for i in range(1,n+1):
        for j in range(1,pattern_size+1):
            print("* ",end="")

        if i<mid:
            pattern_size+=1
        else:
            pattern_size-=1
        
        print()

num = int(input("Enter the row : "))
get_pattern(num)

        