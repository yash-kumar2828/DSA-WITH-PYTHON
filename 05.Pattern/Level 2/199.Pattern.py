'''Enter the number of rows :
7

31 30 29 28 27 26 25 
   24 23 22 21 20 
      19 18 17 
         16 
      15 14 13 
   12 11 10 9  8  
7  6  5  4  3  2  1     '''


def get_pattern(n):
    pattern_size = n
    space = 0
    mid = n//2+1
    num = n*(n+2)//2

    if n%2==0:
        print("Please enter the odd number ")
        return

    for i in range(1,n+1):
        for j in range(1,space+1):
            print(f"{' ':<3}",end="")

        for k in range(1,pattern_size+1):
            print(f"{num:<3}",end="")
            num-=1

        if i<mid:
            pattern_size-=2
            space+=1
        else:
            pattern_size+=2
            space-=1
        print()

num= int(input("Enter the number of rows : "))
get_pattern(num)