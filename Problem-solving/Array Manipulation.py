# sum function to make the prefix sum array
def summer(l,n):
    for i in range(1,len(l)):
        l[i] += l[i-1]
    return l
    

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    L=[0]*n
    m=len(queries)
    for i in range(0,m):
        start = queries[i][0]-1
        end = queries[i][1]-1
        val = queries[i][2]
        if end==(len(L)-1):
            L.append(0)
        L[start]+=val 
        L[end+1]+=-val
    print(L)
    L=summer(L,n)
    return max(L)    

if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)
