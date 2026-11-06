# Print and count all factors of no.

def print_count_factor(n):
    print(1)
    print(n)
    count = 2
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            fact1 = i
            fact2 = n//i
            if fact1!=fact2:
                print(fact1,fact2)
                count = count+2
            else:
                print(fact1)
                count = count+1
       

    print(f"The total factor of {n} is : {count} ")

n = int(input("Enter your number : "))
print_count_factor(n)
