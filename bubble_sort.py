#bubble sort:
'''
Bubble sort is a very simple method that sorts the array elements by repeatedly
moving the largest element to the highest index position of the array segment

note:In every pass, we will compare adjacent elements, if first element is greater than next element, we will swap the two elements

'''
'''
88 14 22 55 41 99 44 10 30 n=9

pass 1: 14 22 55 41 88 44 10 30 99 swap=7

14 88 22 55 41 99 44 10 30
14 22 88 55 41 99 44 10 30
14 22 55 88 41 99 44 10 30
14 22 55 41 88 99 44 10 30
14 22 55 41 88 99 44 10 30
14 22 55 41 88 44 99 10 30
14 22 55 41 88 44 10 99 30
14 22 55 41 88 44 10 30 99
 above is all about pass 1

reamining all pass follows same

pass 2: 14 22 41 55 44 10 30 88 99 swap:4

pass 3: 14 22 41 44 10 30 55 88 99 swap:3

pass 4: 14 22 41 10 30 44 55 88 99 swap:2

pass 5:14 22 10 30 41 44 55 88 99 swap=2

pass 6:14 10 22 30 41 44 55 88 99 swap:1

pass 7:10 14 22 30 41 44 55 88 99 swap:1

pass 8:10 14 22 30 41 44 55 88 99 swap:0

'''
'''
def bubblesort(n,data):
    for i in range(n-1):
        sc=0
        for j in range(n-i-1):
            if data[j]>data[j+1]:
                temp=data[j]
                data[j]=data[j+1]
                data[j+1]=temp
                sc+=1
        print(data)#,sc)
        if sc==0:
            break
    #print(data)

n=int(input())
data=list(map(int,input().split()))
bubblesort(n,data)
'''
'''
9
88 14 22 55 41 99 44 10 30 
[14, 22, 55, 41, 88, 44, 10, 30, 99] 7
[14, 22, 41, 55, 44, 10, 30, 88, 99] 4
[14, 22, 41, 44, 10, 30, 55, 88, 99] 3
[14, 22, 41, 10, 30, 44, 55, 88, 99] 2
[14, 22, 10, 30, 41, 44, 55, 88, 99] 2
[14, 10, 22, 30, 41, 44, 55, 88, 99] 1
[10, 14, 22, 30, 41, 44, 55, 88, 99] 1
[10, 14, 22, 30, 41, 44, 55, 88, 99] 0
[10, 14, 22, 30, 41, 44, 55, 88, 99]

'''
def bubblesort(n,data):
    for i in range(n-1):
        sc=0
        for j in range(n-i-1):
            if data[j]>data[j+1]:
                temp=data[j]
                data[j]=data[j+1]
                data[j+1]=temp
                sc+=1
        print(data)
        if sc==0:
            break

n=int(input())
data=list(map(int,input().split()))
bubblesort(n,data)
    
9
88 14 22 55 41 99 44 10 30
[14, 22, 55, 41, 88, 44, 10, 30, 99]
[14, 22, 41, 55, 44, 10, 30, 88, 99]
[14, 22, 41, 44, 10, 30, 55, 88, 99]
[14, 22, 41, 10, 30, 44, 55, 88, 99]
[14, 22, 10, 30, 41, 44, 55, 88, 99]
[14, 10, 22, 30, 41, 44, 55, 88, 99]
[10, 14, 22, 30, 41, 44, 55, 88, 99]
[10, 14, 22, 30, 41, 44, 55, 88, 99]
