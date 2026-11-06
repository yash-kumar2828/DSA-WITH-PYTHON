'''Enter the number of rows :
7

        4   
      3   3   
    2   2   2   
  1   1   1   1   
    2   2   2   
      3   3   
        4            '''


def get_pattern(n):
    pattern_size = 1
    mid = n//2+1
    space = mid
    num = mid

    if n%2 == 0:
        print("Please enter the odd number")
        return

    for i in range(1,n+1):
        for j in range(1,space+1):
            print(f"{' ':<2}",end="")

        for k in range(1,pattern_size+1):
            print(f"{num:<4}",end="")

        if i<mid:
            pattern_size+=1
            space-=1
            num-=1

        else:
            pattern_size-=1
            space+=1
            num+=1

        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)