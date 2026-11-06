'''Enter the number of rows :
7

      1 
    2   2 
  3       3 
4           4 
  3       3 
    2   2 
      1    '''


def get_pattern(n):

    mid = n//2+1
    left = mid
    right = mid
    num = 1

    if n%2 == 0:
        print("Please enter the odd number ")
        return

    for i in range(1,n+1):

        for j in range(1,right+1):

            if j == left or j == right:
                print(f"{num:<2}",end="")
            else:
                print(f"{' ':<2}",end="")

        if i<mid:
            left-=1
            right+=1
            num+=1

        else:
            left+=1
            right-=1
            num-=1

        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)