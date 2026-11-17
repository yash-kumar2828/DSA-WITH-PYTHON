# WAP to get sum of all elements of array.

def get_sum_of_array(a):
    sum = 0
    for i in range(len(a)):
        sum+=a[i]

    print(f"Sum of array is : {sum}")


a = [1,2,3,4,5,6,7,8,9,10]
get_sum_of_array(a)