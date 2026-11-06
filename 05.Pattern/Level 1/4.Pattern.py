'''Enter the number of rows:
5
1 0 1 0 1
1 0 1 0 1 
1 0 1 0 1
1 0 1 0 1
1 0 1 0 1'''

def get_pattern(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(j%2,end=" ")
        print()

num = int(input("Enter the number of rows : "))
get_pattern(num)