# WAPP to print and count all palindrome number elements of array.
def get_all_palidrome_in_array(a):

    count = 0
    print("Palindrome numbers in array:", end=" ")

    for num in a :

        if num>=0:
            temp = num
            rev =  0

            while num>0:
                rem = num%10
                rev = rev*10 + rem
                num//=10

            if rev == temp:
                print(temp,end=" ")
                count+=1

    print(f"\nTotal palidrome is : {count}")


arr = [121, 345, 7, 44, 12321, 90, -121, 1001]
get_all_palidrome_in_array(arr)