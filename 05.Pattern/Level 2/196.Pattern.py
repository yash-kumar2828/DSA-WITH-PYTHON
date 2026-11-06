'''Enter the number of rows :
7

1  2  3  4  5  6  7  
   1  2  3  4  5  
      1  2  3  
         1  
      1  2  3  
   1  2  3  4  5  
1  2  3  4  5  6  7  '''


def get_pattern(n):
    pattern_size = n
    space = 0
    mid = n//2+1

    if n%2==0:
        print("Please enter the odd number ")
        return

    for i in range(1,n+1):
        for j in range(1,space+1):
            print(f"{' ':<3}",end="")

        for k in range(1,pattern_size+1):
            print(f"{k:<3}",end="")

        if i<mid:
            pattern_size-=2
            space+=1
        else:
            pattern_size+=2
            space-=1
        print()

num= int(input("Enter the number of rows : "))
get_pattern(num)