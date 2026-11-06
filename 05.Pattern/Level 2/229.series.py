'''Print the below series :
1,2,5,26,677. ......'''


def get_series(n):

    num = 1

    for i in range(1,n+1):
        print(f"{num:<4}",end="")
        num = (num**2) + 1


num = int(input("Enter the number of series : "))
get_series(num)