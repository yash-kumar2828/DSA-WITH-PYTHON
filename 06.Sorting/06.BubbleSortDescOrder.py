def bubble_sort_desc_order(a):

    for i in range(len(a)-1):
        flag = True

        for j in range(len(a)-i-1):
            if a[j]<a[j+1]:
                a[j],a[j+1] = a[j+1] , a[j]
                flag = False

        if flag:
            return


a = [10,12,21,34,10,23,5,6,9]
print(f"Original Array : {a}")
bubble_sort_desc_order(a)
print(f"After sorting array : {a}")