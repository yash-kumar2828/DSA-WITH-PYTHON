def merge(a,start,mid,end):
    merged = [a]*(end-start+1)
    i,j,k = start, mid+1,0

    while i<=mid and j<=end:
        if a[i]<a[j]:
            merged[k] = a[i]
            i+=1
            k+=1
        else:
            merged[k] = a[j]
            k+=1
            j+=1


    while i<=mid:
        merged[k] = a[i]
        k+=1
        i+=1

    while j<=end:
        merged[k] = a[j]
        k+=1
        j+=1

    index1 = 0
    index2 = start
    while index1<len(merged):
        a[index2] = merged[index1]
        index1+=1
        index2+=1


def merge_sort(a,start,end):
    if start<end:
        mid = (start+end)//2
        merge_sort(a,start,mid)
        merge_sort(a,mid+1,end)
        merge(a,start,mid,end)


a = [10,12,21,34,10,23,5,6,9]
print(f"Original Array : {a}")
merge_sort(a,0,len(a)-1)
print(f"After sorting array : {a}")
    