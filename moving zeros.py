#movie zeros
'''
def movezeros(n,data):
    i=0
    for j in range(n):
        if arr[j]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
n=int(input())
arr=list(map(int,input().split()))
movezeros(n,arr)
print(*arr)


6
1 7 0 0 0 2
1 7 2 0 0 0
>>>
'''

def movezeros(n,data):
    zc=0
    for i in data:
        if i==0:
            data.remove(i)
            data.append(0)
n=int(input())
data=list(map(int,input().split()))
movezeros(n,data)
print(*data)

