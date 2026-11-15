'''Enter the number of rows :
11

@   @   @   @   @   @   @   @   @   @   *   
*   @   @   @   @   @   @   @   @   *   *   
*   *   @   @   @   @   @   @   *   *   *   
*   *   *   @   @   @   @   *   *   *   *   
*   *   *   *   @   @   *   *   *   *   *   
*   *   *   *   *   *   *   *   *   *   *   
*   *   *   *   @   @   *   *   *   *   *   
*   *   *   @   @   @   @   *   *   *   *   
*   *   @   @   @   @   @   @   *   *   *   
*   @   @   @   @   @   @   @   @   *   *   
@   @   @   @   @   @   @   @   @   @   * 
'''


def get_pattern(n):
    mid = n//2+1
    left = 1
    right = n

    for i in range(1,n+1):

        for j in range(1,n+1):

            if j+1<=left or j>=right:
                print(f"{'*':<4}",end='')

            else:
                print(f"{'@':<4}",end='')

        if i<mid:
            left+=1
            right-=1
        else:
            left-=1
            right+=1
        print()


num = int(input("Enter the number of rows : "))
get_pattern(num)