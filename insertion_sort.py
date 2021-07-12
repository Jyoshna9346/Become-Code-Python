'''
#insertion sort: it is a sorting algorithm in which the sorted array or list is bulit one element at a time

#points:

1.first we take elements as sorted
2.then we take every element and campare it with previous elements
and insert it in correct place
3.that'y it is called as insertion sort



88 14 22 55 41 99 44 10 34

pass 0: 88 14 22 55 41 99 44 10 34 

pass 1: 14 88 22 55 41 99 44 10 34 #compare 1st 2 two numbers

pass 2: 14 22 88 55 41 99 44 10 34 #compare 1st 3 numbers

pass 3: 14 22 55 88 41 99 44 10 34 #compare 1st 4 numbers 

pass 4: 14 22 41 55 88 99 44 10 34 #compare 1st 5 numbers

pass 5: 14 22 41 55 88 99 44 10 34 #compare 1st 6 numbers

pass 6: 14 22 41 44 55 88 99 10 34 #compare 1st 7 numbers

pass 7: 10 14 22 41 44 55 88 99 34 #compare 1st 8 numbers

pass 8: 10 14 22 34 41 44 55 88 99 #compare 1st 8 numbers

'''
'''
algorithm
14 22 41 44 55 88 99 10 34

key=44 or 13 
 if key>data[j]:
     data[j+1]=key
     stop here
else:
    data[j+1]=data[j]
    j-=1


if data[i]<data[i-1]:
    key=10
if key>data[j]:
    data[j+1]=key
    break
else:
    data[j+1]=data[j]
    if j==0:
        data[j]=key
    i-=1
'''
#program

def insertionsort(n,data):
    for i in range(1,n):
        key=data[i]
        for j in range(i-1,-1,-1):
            if key>data[j]:
                data[j+1]=key
                break
            else:
                data[j+1]=data[j]
        else:
            data[0]=key
    print(data)
n=int(input())
data=list(map(int,input().split()))
insertionsort(n,data)
'''
9
88 14 22 55 41 99 44 10 30 
[10, 14, 22, 30, 41, 44, 55, 88, 99]
'''
 =======
def insertionsort(n,data):
    for i in range(1,n):
        key=data[i]
        for j in range(i-1,-1,-1):
            if key>data[j]:
                data[j+1]=key
                break
            else:
                data[j+1]=data[j]
        else:
            data[0]=key
        print(data)
n=int(input())
data=list(map(int,input().split()))
insertionsort(n,data)
 
9
88 14 22 55 41 99 44 10 30
[14, 88, 22, 55, 41, 99, 44, 10, 30]
[14, 22, 88, 55, 41, 99, 44, 10, 30]
[14, 22, 55, 88, 41, 99, 44, 10, 30]
[14, 22, 41, 55, 88, 99, 44, 10, 30]
[14, 22, 41, 55, 88, 99, 44, 10, 30]
[14, 22, 41, 44, 55, 88, 99, 10, 30]
[10, 14, 22, 41, 44, 55, 88, 99, 30]
[10, 14, 22, 30, 41, 44, 55, 88, 99]
>>> 


