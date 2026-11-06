'''Print the below series :
1,3,7,13,21,......'''


def get_series(n):
    num = 1
    diff = 2

    for i in range(n):

        print(f"{num:<3}",end="")

        num+=diff
        diff+=2

num = int(input("Enter the number of series : "))
get_series(num)
     