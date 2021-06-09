#maximum of number of ones in a program

def max_sorted_length(n,data):
    if n==0:
        return 0
    c=1
    count=0
    for i in range(n-1):
        if data[i]==1:
           if data[i]==data[i+1]:
               c+=1
        else:
            if count<c:
                count=c
            c=1
    return max(c,count)
n=int(input())
data=list(map(int,input().split()))
print(max_sorted_length(n,data))
