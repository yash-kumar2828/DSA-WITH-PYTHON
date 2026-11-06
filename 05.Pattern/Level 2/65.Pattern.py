'''Enter the number of rows :
5
        A
      B C 
    D E F 
  G H I J
K L M N O   '''

def get_pattern(n):
    pattern_size = 1
    space = n-1

    alpha = 65
    for i in range(1,n+1):
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
