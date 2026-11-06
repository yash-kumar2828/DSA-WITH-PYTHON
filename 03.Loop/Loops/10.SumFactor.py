# WAP sum of all factors of number

def sumFactors(num):
    sum = 0
    for i in range(1,int(num**0.5)+1):
        if num%i==0:
            fact1 = i
            fact2 = num//i
            if fact1!=fact2:
                print(fact1,fact2,end=' ')
                sum = sum+fact1+fact2
            else:
                print(fact1)
                sum = sum+fact1

    print(f"\nFactor sum is : {sum}")


num = int(input("Enter your number : "))
sumFactors(num)

