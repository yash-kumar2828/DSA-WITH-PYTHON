'''Print the below series :
2 5 11 23 47 95 191 383 767 1535'''


def get_series(n):
    num = 2

    for i in range(1,n+1):
        print(f"{num:<4}",end="")
        num = num*2 + 1

num = int(input("Enter the number of series : "))
get_series(num)


