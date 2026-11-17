def heapify(a,i,n):
    max = i
    left = 2*i+1
    right = 2*i+2

    if left<n and a[left] > a[max]:
        max = left

    if right<n and a[right] > a[max]:
        max = right

    if i!=max:
        a[i], a[max] = a[max], a[i]
        heapify(a,max,n)


def heap_sort_asc_order(a):
    n = len(a)
    i = n//2-1
    while i>=0:
        heapify(a,i,n)
        i-=1

    j = n-1
    while j>=0:
        a[0],a[j] = a[j],a[0]
        heapify(a,0,j)
        j-=1


a = [10,12,21,34,10,23,5,6,9]
print(f"Original Array : {a}")
heap_sort_asc_order(a)
print(f"After sorting array : {a}")