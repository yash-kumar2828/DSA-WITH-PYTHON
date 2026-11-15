'''Enter the number of rows :
5

A  
C  B  
D  E  F  
J  I  H  G  
K  L  M  N  O 

'''

def get_pattern(n):
    alpha = 65
    patternSize = 1

    for i in range(1,n+1):

        if i%2 != 0:
            for j in range(0,patternSize):
                print(f"{chr(alpha+j):<3}",end="")

        else:
            for j in range(patternSize-1, -1, -1):
                print(f"{chr(alpha+j):<3}",end="")

        alpha+=i
        patternSize+=1
        print()


num = int(input("Enter the number of rows : "))
get_pattern(num)
