def insertion_sort_desc_order(a):

    for i in range(1,len(a)):
        max_element = a[i]

        j = i-1

        while j>=0 and a[j]<max_element:
            a[j+1] = a[j]
            j-=1

        a[j+1] = max_element

a = [10,12,21,34,10,23,5,6,9]
print(f"Original Array : {a}")
insertion_sort_desc_order(a)
print(f"After sorting array : {a}")