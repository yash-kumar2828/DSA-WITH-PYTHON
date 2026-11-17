# WAP to get average of all elements of array.

def get_average_of_array(a):

    sum = 0

    for i in range(len(a)):
        sum+=a[i]

    average = sum/len(a)
    print(f"Average of array is : {average}")

a = [1,2,3,4,5,6,7,8,9,10]
get_average_of_array(a)