# to print max and min element of array.

def get_min_max_element(a):
    min_element = a[0]
    max_element = a[0]

    for i in range(len(a)):
        if a[i]<min_element:
            min_element = a[i]
        elif a[i]>max_element:
            max_element = a[i]

    print(f"Min element is : {min_element}")
    print(f"Maximum element is : {max_element}")
        


a = [10,12,33,12,90,12,5,100,101,90]
get_min_max_element(a)