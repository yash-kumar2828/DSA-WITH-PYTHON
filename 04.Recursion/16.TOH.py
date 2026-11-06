# WAPP to solve Tower Of Hanoi problem.

def TOH(n,s,aux,d):
    if n==1:
        print(f"Move disk from {s} to {d}")
        return
    

    TOH(n-1,s,d,aux)
    print(f"Move disk from {s} to {d}")
    TOH(n-1,aux,s,d)


n = int(input("Enter your number : "))
TOH(n,'A','B','C')