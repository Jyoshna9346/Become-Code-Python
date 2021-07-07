#binary search: 'it will work with sorted form
'''
with low ,high,mid values

10

1 2 3 4 5 6 7 8 9 10
0 1 2 3 4 5 6 7 8 9
l=0
h=n-1=9
mid=l+h/2
it returns index value if it found key in give sorted data

l=m+1-->key>mid
h=m-1-->key<mid
'''
#normal_method
'''
n=int(input())
data=list(map(int,input().split()))
key=int(input())
data.sort()
l,h=0,n-1
m=(1+h)//2
for i in range(n):
    if data[m]==key:
        print("FOUND")
        break
    if key<data[m]:
        h=m-1
        m=(1+h)//2
        if data[m]==key:
            print("FOUND")
            break
    if key>data[m]:
        l=m+1
        m=(l+h)//2
        if data[m]==key:
            print("FOUND")
            break
else:
    print("NOT FOUND")

8
22 34 55 66 88 546 345 66 
99
NOT FOUND
>>> 
=======
8
22 34 55 66 88 546 345 66 
88
FOUND
'''
#using function
'''
def binary_search(n,data,key):
    l=0
    h=n-1
    while l<=h:
        m=(l+h)//2
        if key==data[m]:
            return True
        if key<data[m]:
            h=m-1
        else:
            l=m+1
    print(l,h)
    return False
n=int(input())
data=list(map(int,input().split()))
key=int(input())
print(binary_search(n,data,key))

9
12 34 32 454 32 17 65 43 87
32
True
>>> 
========
9
12 34 32 454 32 17 65 43 87
99
9 8
False
'''
#oops concept
class search:
    def __init__(self,n,data,key):
        self.size=n
        self.data=data
        self.key=key
    def linearsearch(self):
        c=0
        for i in self.data:
            if i==self.key:
                return True
        print(c)
        return False
    def binarysearch(self):
        self.data.sort()
        l=0
        h=n-1
        c=0
        while l<=h:
            m=(l+h)//2
            if self.key==self.data[m]:
                return True
            if self.key<self.data[m]:
                h=m-1
            else:
                l=m+1
        print(l,h)
        print(c)
        return False
n=int(input())
data=list(map(int,input().split()))
key=int(input())
s1=search(n,data,key)#obj creation
print(s1.linearsearch())
print(s1.binarysearch())

9
12 34 545 32 16 17 43 87 99
32
True
True
>>> 
========
9
12 34 545 32 16 17 43 87 99
100
0
False
8 7
0
False

