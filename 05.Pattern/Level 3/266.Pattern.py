'''Enter the nunber of rows :
7

4  4  4  4  4  4  4  
4  3  3  3  3  3  4  
4  3  2  2  2  3  4  
4  3  2  1  2  3  4  
4  3  2  2  2  3  4  
4  3  3  3  3  3  4  
4  4  4  4  4  4  4 

'''


def get_pattern(n):
    mid = n//2+1
    num = mid
    left = 1
    right = n

    if n%2==0:
        print("Please enter the odd number")
        return
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j<left:
                print(f"{num:<3}",end="")
                num-=1

            elif j>right:
                num+=1
                print(f"{num:<3}",end="")

            else:
                print(f"{num:<3}",end="")
        
        if i<mid:
            left+=1
            right-=1
        else:
            left-=1
            right+=1
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)