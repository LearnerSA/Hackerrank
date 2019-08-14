import copy

def swap(list, pos1, pos2): 
      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list

def lilysHomework(arr):
    n=len(arr)
    pos={}
    pos2= copy.deepcopy(pos)
    count1=0
    count2=0
    arrcopy = arr[:]
    
    for x in range(0,n):
        pos[arr[x]]=x
    
        
    #print(pos)
        
    for x in range(0,n):
        if arr == check:
            break
        if arr[x] != check[x]:
            count1+=1
            firstindex = pos[arr[x]]
            secondindex = pos[check[x]]
            #print(firstindex,secondindex)
            pos[arr[x]]=secondindex
            pos[check[x]]=firstindex
            arr = swap(arr,firstindex,secondindex)
            
            #print(arr,"---")
    firstindex=0
    secondindex=0
    
    for x in range(0,n):
        if arrcopy == checkback:
            break
        if arrcopy[x] != checkback[x]:
            count2+=1
            firstindex = pos2[arrcopy[x]]
            secondindex = pos2[checkback[x]]
            #print(firstindex,secondindex)
            pos2[arrcopy[x]]=secondindex
            pos2[check[x]]=firstindex
            #print(pos2)
            arrcopy = swap(arrcopy,firstindex,secondindex)
            print(arrcopy,"---")
            
    return min(count1,count2)
            

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    check = sorted(arr)
    checkback = sorted(arr , reverse = True)
    #n=len(arr)
    print("ascending",check,"descending",checkback)

    result = lilysHomework(arr)
    print(result)
