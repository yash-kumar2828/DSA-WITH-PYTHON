'''WAP to  swap two index values of the array. Swap index 1 and 5 elements:
Original array: 10 20 30 40 50 60 70
Swapped array:  10 60 30 40 50 20 70
'''

def swap_two_index(a):
    a[1],a[5] = a[5],a[1]

a = [10,20,30,40,50,60,70]
print(f"Original array : {a}")
swap_two_index(a)
print(f"Swapped array : {a}")

