# 1 * 2**2 + 2 * 3**2 + 3 * 4**2+ .......upto 100

def sumSeries(n):
    if n == 1:
        return (1 * (2**2))

    return (n*(n+1)**2)+sumSeries(n-1)

num = int(input("Enter your number : "))
res = sumSeries(num)
print(f"Sum of series is : {res}")