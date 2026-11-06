'''Enter the number of rows : 
7

7  6  5  4  3  2  1  
   5  4  3  2  1  
      3  2  1  
         1  
      3  2  1  
   5  4  3  2  1  
7  6  5  4  3  2  1      '''


def get_pattern(n):
    pattern_size = n
    mid = n//2+1
    space = 0

    if n%2==0:
        print("Please enter the odd number : ")
        return

    for i in range(1,n+1):
        for j in range(1,space+1):
            print(f"{' ':<3}",end="")

        num = pattern_size

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

num = int(input("Enter the number of rows : "))
get_pattern(num)

