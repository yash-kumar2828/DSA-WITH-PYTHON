def selection_sort_desc_order(a):

    for i in range(len(a)):
        max_element = a[i]
        max_index = i

        for j in range(i+1,len(a)):

            if a[j] > max_element:
                max_element = a[j]
                max_index = j

        a[max_index] , a[i] = a[i], a[max_index]

a = [10,12,21,34,10,23,5,6,9]
print(f"Original Array : {a}")
selection_sort_desc_order(a)
print(f"After sorting array : {a}")