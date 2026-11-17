# WAP to get average of all elements at even index of array.

def get_average_of_all_even_element(a):

    sum = 0
    count = 0
    for i in range(len(a)):

        if i%2 == 0:
            sum+=a[i]
            count+=1

    average = sum/count
    print(f"Average of all elements at even index of array : {average}")

a = [1,2,3,4,5,6,7,8,9,10]
get_average_of_all_even_element(a)
    