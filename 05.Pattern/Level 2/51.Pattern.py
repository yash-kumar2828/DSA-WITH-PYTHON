'''Enter the number of rows : 
5

E
D D 
C C C 
B B B B 
A A A A A  '''

def get_pattern(n):
    pattern_size = 1
    alpha = 65 + n - 1

    for i in range(1,n+1):
        for j in range(1,pattern_size+1):
            print(f"{chr(alpha)} ",end="")

        alpha-=1
        pattern_size+=1
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)
