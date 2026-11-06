'''Print the below series :
1,2,6,7,21,22,66,........'''


def get_series(n):

    num = 1

    for i in range(1,n+1):

        print(f"{num:<4}",end="")

        if i%2 != 0:
            num+=1

        else:
            num*=3


num = int(input("Enter the number of series : "))
get_series(num)
