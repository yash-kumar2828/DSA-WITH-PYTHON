'''Enter the number of rows:
7 
            *   
          *   *   
        *   *   *   
      *   *   *   *   
    *   *   *   *   *   
  *   *   *   *   *   *   
*   *   *   *   *   *   *      '''

def get_pattern(n):
    space = n-1
    pattern_size = 1

    for i in range(1,n+1):
        for j in range(1,space+1):
            print(f"{' ':<2}",end="")

        for k in range(1,pattern_size+1):
            print(f"{"*":<4}",end="")
        
        space-=1
        pattern_size+=1
        print()


num =int(input("Enter the number of rows : "))
get_pattern(num)
