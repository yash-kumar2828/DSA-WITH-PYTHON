'''Print the below Series:
2,6,12,20,30,42, ........'''


def get_series(n):

    for i in range(1,n+1):
        res = i*i+i
        print(f"{res:<3}",end="")

num = int(input("Enter the number of series : "))
get_series(num)