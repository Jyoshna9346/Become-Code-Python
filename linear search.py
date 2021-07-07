'''
2 types of searching
  1.linear search
  2.binary search
'''


#linear seraching:'sequential search -->used for unorderd or unsorted list 

#normal ways

'''
n=int(input())
data=list(map(int,input().split()))
key=int(input())
for i in data:
        if key==i:
            print("FOUND")
            break
else:
    print("NOT FOUND")


    
8
13 45 67 23 55 67 77 88 
100
NOT FOUND
>>> 
8=n
0   1  2  3  4 5  6  7-->index values
13 45 67 23 55 67 77 88
55
FOUND
'''
#using function concepts
'''
def linearsearch(n,data,key):
    for i in data:
        if key==i:
            return True
    return False
n=int(input())
data=list(map(int,input().split()))
key=int(input())
print(linearsearch(n,data,key))

8
13 45 67 23 55 67 77 88
55
True
>>> 
============
8
13 45 67 23 55 67 77 88
100
False
'''
#oops concepts
class search:
    def __init__(self,n,data,key):
        self.size=n
        self.data=data
        self.key=key
    def linearsearch(self):
        for i in self.data:
            if i==self.key:
                return True
        return False
n=int(input())
data=list(map(int,input().split()))
key=int(input())
s1=search(n,data,key)
print(s1.linearsearch())

8
13 45 67 23 55 67 77 88
55
True
>>> 
======
8
13 45 67 23 55 67 77 88
100
False

        
        
