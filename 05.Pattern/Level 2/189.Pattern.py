'''Enter the number of rows :
7

            Y  
         X  W  V  
      U  T  S  R  Q  
   P  O  N  M  L  K  J  
      I  H  G  F  E  
         D  C  B  
            A      '''


def get_pattern(n):
    pattern_size = 1
    mid = n//2+1
    space = mid
    alpha = 65 + (n**2)//2

    if n%2 == 0:
        print("Please enter the odd number")
        return


    for i in range(1,n+1):

        for j in range(1,space+1):
            print(f"{' ':<3}",end="")

        for k in range(1,pattern_size+1):
            print(f"{chr(alpha):<3}",end="")
            alpha-=1

        if i<mid:
            pattern_size+=2
            space-=1

        else:
            pattern_size-=2
            space+=1

        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)