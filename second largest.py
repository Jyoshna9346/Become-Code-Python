#second largest element
def secondlargest(n,data):
    sh,lh=data[0],data[0]
    for i in data[1:]:
        if data[i]>fh:
            sh=fh
            fh=data[i]
        if data[i]>sh and data[i]fh:
            sh=i
         
    return sh

n=int(input())
data=list(map(int,input().split()))
print(secondlargest(n,data))

