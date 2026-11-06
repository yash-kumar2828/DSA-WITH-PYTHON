# 1**2 * 2 + 2**2 * 3 + 3**2 * 4+ ..........upto 100

def sumSeries(n):
    if n==1:
        return (1**2 * 2)

    return (n**2 * (n+1))+sumSeries(n-1)

num = int(input("Enter your number : "))
res = sumSeries(num)
print(f"Sum of series is : {res}")