'''Print the below Fibonacci series
0,1,1,2,3,5,8,13,21'''

def get_fibonacci_series(n):

    a = 0
    b = 1
    print(a,b,end=" ")

    for i in range(n-2):
        c = a+b
        print(f"{c}",end=" ")
        a = b
        b = c


num = int(input("Enter the number of rows : "))
get_fibonacci_series(num)