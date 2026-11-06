'''Enter the number of rows :
5
        O
      M N 
    J K L 
  F G H I 
A B C D E   '''

def get_pattern(n):
    pattern_size = 1
    space = n-1

    for i in range(1,n+1):
        alpha = 65 + (n*(n+1)//2) - (i*(i+1)//2)

        for j in range(1,space+1):
            print("  ",end="")

        for k in range(1,pattern_size+1):
            print(f"{chr(alpha)} ",end="")
            alpha+=1

        pattern_size+=1
        space-=1
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)


