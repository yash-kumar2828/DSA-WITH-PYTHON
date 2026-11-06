# WAP to print and count palidrome number in range

def isPrime(num):
    rev = 0
    temp = num
    while num>0:
        rem = num%10
        rev = rev*10+rem
        num = num//10
    return temp == rev


def print_and_count_palidrome(start,end):
    count = 0
    for i in range(start,end+1):
        if isPrime(i):
            print(i,end=" ")
            count+=1
    print(f"\nTotal palidrome number is : {count}")


start = int(input("Enter starting value : "))
end = int(input("Enter ending value : "))

print_and_count_palidrome(start,end)