'''Enter the number of rows :
7

              1   
            1   1   
          1   2   1   
        1   3   3   1   
      1   4   6   4   1   
    1   5   10  10  5   1   
  1   6   15  20  15  6   1   
1   7   21  35  35  21  7   1  

'''


def pascal_row(n):
    comb =1
    print(f"{comb:<4}",end="")
    for i in range(n):
        comb = comb*(n-i)//(i+1)
        print(f"{comb:<4}",end='')


def pascal_triangle(n):
    space = n
    for i in range(n+1):
        for j in range(space):
            print(f"{' ':<2}",end="")
        pascal_row(i)
        space-=1
        print()


num = int(input("Enter the number of rows : "))
pascal_triangle(num)