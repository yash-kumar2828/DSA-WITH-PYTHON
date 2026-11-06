'''Enter the number of rows :
5

E   D   C   B   A   
  D   C   B   A   
    C   B   A   
      B   A   
        A      '''


def get_pattern(n):

    pattern_size = n
    space = 0
    

    for i in range(1,n+1):
        alpha = 65+n-i
        for j in range(1,space+1):
            print(f"{' ':<2}",end="")

        for k in range(1,pattern_size+1):
            print(f"{chr(alpha):<4}",end="")
            alpha-=1

        pattern_size-=1
        space+=1
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)