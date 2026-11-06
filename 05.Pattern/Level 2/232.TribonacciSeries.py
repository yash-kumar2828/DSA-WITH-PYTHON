'''Print the below Tribonacci Series :
0,1,1,2,4,7,13,24,.......'''


def get_tribonacci_series(n):
    a = 0
    b = 1
    c = 1
    print(a,b,c,end=" ")

    for i in range(n-3):
        d = a+b+c

        print(f"{d}",end=" ")

        a = b
        b = c 
        c = d

num = int(input("Enter the number of series : "))
get_tribonacci_series(num)