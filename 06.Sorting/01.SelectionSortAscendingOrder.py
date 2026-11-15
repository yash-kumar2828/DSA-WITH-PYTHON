def selection_sort_asc_order(a):
    for i in range(len(a)):
        min_element = a[i]
        min_index = i
        for j in range(i+1,len(a)):
            if a[j]<min_element:
                min_element = a[j]
                min_index = j

        a[min_index], a[i] = a[i], a[min_index]

a = [10,12,21,34,10,23,5,6,9]
print(f"Original Array : {a}")
selection_sort_asc_order(a)
print(f"After sorting array : {a}")
