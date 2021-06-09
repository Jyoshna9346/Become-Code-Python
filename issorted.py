'''
>>> sorted(data)
[1, 2, 3, 4, 7, 8]
>>> data=[1,2,3,4,7,8]
>>> data==sorted(data)
True
'''

#sorted or not

def issorted(n,data):
    asc=0
    des=0
    for i in range(n-1):
        if data[i]>=data[i+1]:
            des+=1
        if data[i]<=data[i+1]:
            asc+=1
        if des!=0 and asc!=0:
            return False
    return True
n=int(input())
data=list(map(int,input().split()))

'''
def issorted(data):
    temp1=data.copy()
    temp2=data.copy()
    temp1.sort()
    temp2.sort(reverse=True)
    return(data==temp1 or data==temp2)
data=list(map(int,input().split()))
print(issorted(data))


1 2 2 3 4
True
>>> 
=================
4 5 6 7 8 9 2 3 4 
False
'''
