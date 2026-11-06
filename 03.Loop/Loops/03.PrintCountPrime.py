# WAP to print and count the prime number in range.

def isPrime(n):
    if n<2:
        return False
    elif n == 2:
        return True
    elif n%2 == 0:
        return False
    else:
        for i in range(3,int(n**0.5)+1,2):
            if n%i == 0:
                return False
        return True


def print_and_count_prime(start,end):
    count = 0
    for i in range(start,end+1):
        if isPrime(i):
            print(i,end=" ")
            count+=1

    print(f"\nThe total prime number is : {count}")

start = int(input("Enter your starting value : "))
end = int(input("Enter your ending value : "))

print_and_count_prime(start,end)
