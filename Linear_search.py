def linear_search(data,key):
    count=0
    for i in range(0,len(data)):
        count+=1
        if data[i]==key:
            print("Element found")
            return count
    else:
        print("Not found")
        return count
def binary_search(data,key):
    l=0
    h=len(data)-1
    count=0
    while(l<=h):
        count+=1
        m=(l+h)//2
        if data[m]==key:
            print("Element found")
            return count
        elif data[m]>key:
            h=m-1
        else:
            l=m+1
    else:
        print("Not found")
        return count



data=list(map(int,input().split()))
key=int(input())
#print(linear_search(data,key))
print(binary_search(data,key))

