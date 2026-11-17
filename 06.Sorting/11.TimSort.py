def tim_sort_asc_order(a):
    a.sort()
    print(f"Ascending Order : {a}")



def tim_sort_desc_order(a):
    a.sort(reverse = True)
    print(f"Descending Order : {a}")



a = [9,8,5,3,4,6,7,2,1]
tim_sort_asc_order(a)
tim_sort_desc_order(a)
