'''
#selection sort: it is sorting algorithm 
it is used in both ascending and descending order
'''
#for example:

#descending order
'''
0  1   2  3  4 5  6  7  8 
78 12 14 24 34 88 66 22 35
         0  1  2  3 4  5  6  7  8
pass 1: 78 12 14 24 34 35 66 22 88  
pass 2: 22 12 14 24 34 35 66 78 88 
pass 3: 22 12 14 24 34 35 66 78 88
pass 4: 22 12 14 24 34 35 66 78 88
pass 5: 22 12 14 24 34 35 66 78 88
pass 6: 22 12 14 24 34 35 66 78 88
pass 7: 14 12 22 24 34 35 66 78 88
pass 8: 12 14 22 24 34 35 66 78 88
'''
#ascending order 
'''
39 9 81 45 90 27 72 18
       0 1  2  3  4  5  6   7 position 
pass 1:9 39 81 45 90 27 72 18 1
pass 2:9 18 81 45 90 27 72 39 7             
pass 3:9 18 27 45 90 81 72 39 5
pass 4:9 18 27 39 90 81 72 45 7
pass 5:9 18 27 39 45 81 72 90 7
pass 6:9 18 27 39 45 72 81 90 6
pass 7:9 18 27 39 45 72 81 90 6

'''
#using function

#highest to lowest
'''
def selectsort(arr,n):
    x=max(data)
    for i in range(1,n):
        data[-i],data[data.index(x)]=data[data.index(x)],data[-i]
        x=max(data[:-i])
        print(arr)
data=list(map(int,input().split()))
selectsort(data,len(data))


55 44 22 77 66 55 11 33 32
[55, 44, 22, 32, 66, 55, 11, 33, 77]
[55, 44, 22, 32, 33, 55, 11, 66, 77]
[11, 44, 22, 32, 33, 55, 55, 66, 77]
[11, 44, 22, 32, 33, 55, 55, 66, 77]
[11, 33, 22, 32, 44, 55, 55, 66, 77]
[11, 32, 22, 33, 44, 55, 55, 66, 77]
[11, 22, 32, 33, 44, 55, 55, 66, 77]
[11, 22, 32, 33, 44, 55, 55, 66, 77]

'''
'''
class selectionsort():
    def __init__(self,l):
        self.l=1
    def sorting(self):
        i=0
        while i<len(self.l)-1:
            if i==0:
                m=max(self.l)
                self.l[-1],self.l[self.l.index(m)]=self.l[self.l.index(m)],self.l[-1]
                print('pass '+str(i+1)+':',*self.l)
            else:
                m=max(self.l[:-i])
                self.l[-i-1],self.l[self.l.index(m)]=self.l[self.l.index(m)],self.l[-i-1]
                print('pass '+str(i+1)+':',*self.l)
            i+=1
l=list(map(int,input().split()))
sl=selectionsort(1)
sl.sorting()
'''

#oops concepts

def maxi(data,n):
    mi=0
    me=data[0]
    for i in range(1,n):
        if me<data[i]:
            me=data[i]
            mi=i
    return mi
def selectionsort(n,data):
    print(data)
    j=n-1
    for i in range(n-1):
        mi=maxi(data,n-i)
        data[mi],data[j]=data[j],data[mi]
        j-=1
        print(data)
n=int(input())
data=list(map(int,input().split()))
selectionsort(n,data)

9
55 44 22 77 66 55 11 33 32
[55, 44, 22, 77, 66, 55, 11, 33, 32]
[55, 44, 22, 32, 66, 55, 11, 33, 77]
[55, 44, 22, 32, 33, 55, 11, 66, 77]
[11, 44, 22, 32, 33, 55, 55, 66, 77]
[11, 44, 22, 32, 33, 55, 55, 66, 77]
[11, 33, 22, 32, 44, 55, 55, 66, 77]
[11, 32, 22, 33, 44, 55, 55, 66, 77]
[11, 22, 32, 33, 44, 55, 55, 66, 77]
[11, 22, 32, 33, 44, 55, 55, 66, 77]

    
    
