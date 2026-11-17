# WAP to print and count all prime number elements of array.


def get_all_prime_in_array(a):

    count = 0

    print("Prime numbers in array : ",end=" ")

    for nums in a:
        if nums>1:
            is_prime = True
            i = 2

            while i*i <= nums:
                if nums%i == 0:
                    is_prime = False
                    break
                i+=1
            if is_prime:
                print(nums,end=" ")
                count+=1

    print(f"\nTotal count of prime numbers : {count}")


a = [1,2,3,4,5,6,7,8,9,10]
get_all_prime_in_array(a)


            
        
        