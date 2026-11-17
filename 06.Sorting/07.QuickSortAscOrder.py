def partition(a,start,end):
    pivot = a[start]
    a[start],a[end] = a[end],a[start]
    i = start-1
    j = start

    while j<end:
        if a[j]<pivot:
            i+=1
            a[i],a[j] = a[j],a[i]

        j+=1

    a[i+1],a[end] = a[end],a[i+1]
    return i+1


def quick_sort_asc_order(a,start,end):

    if start<end:
        partitionIndex = partition(a,start,end)
        quick_sort_asc_order(a,start,partitionIndex-1)
        quick_sort_asc_order(a,partitionIndex+1,end)


a = [10,12,21,34,10,23,5,6,9]
print(f"Original Array : {a}")
quick_sort_asc_order(a,0,len(a)-1)
print(f"After sorting array : {a}")