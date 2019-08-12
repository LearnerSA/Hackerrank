import os
import math
import re

def swap(list, pos1, pos2): 
      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list

def lilysHomework(arr):
    i=0
    count1=0
    j=0
    count2=0
    arrcopy=arr[:]
    while i<n:
        if arr==check:
            break
        else:
            A=[]
            head = i
            A=arr[i+1:]
            minimum = A.index(min(A))
            if A[minimum] < arr[head]:
                arr=swap(arr,head,(minimum+i+1))
                count1+=1
        i+=1
    while j<n:
        if arrcopy==checkback:
            break
        else:
            A=[]
            head = j
            A=arrcopy[j+1:]
            maximum = A.index(max(A))
            if A[maximum] > arrcopy[head]:
                arrcopy=swap(arrcopy,head,(maximum+j+1))
                count2+=1
        j+=1
    return min(count2,count1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    check = sorted(arr)
    checkback = sorted(arr , reverse = True)


    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
