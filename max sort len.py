#maxsort

def maxsortlen(n,arr):
    if n==0:
        return 0
    count=1
    c=1
    for i in range(n-1):
        if arr[i]<arr[i+1]:
            c+=1
        else:
            if count<c:
                count=c
            c=1
    return max(c,count)
n=int(input())
data=list(map(int,input().split()))
print(maxsortlen(n,data))
