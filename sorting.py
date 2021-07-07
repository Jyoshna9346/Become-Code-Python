"""
selection sort
insertion sort
bubble sort
"""
def insertion_sort(data):
    for i in range(1,len(data)):
        temp=data[i]
        for j in range(i-1,-1,-1):
            if data[j]>temp:
                data[j+1]=data[j]
            else:
                data[j+1]=temp
                break
        else:
            data[0]=temp
        print(data)
            
    
def selection_sort(data):
    for i in range(len(data)-1,0,-1):# for i in range(6,0,-1): 5
        me=data[i]
        mind=i
        for j in range(i,-1,-1):
            if data[j]>me:
                me=data[j]
                mind=j
        temp=data[mind]
        data[mind]=data[i]
        data[i]=temp
        print(data)
        
        
data=list(map(int,input().split()))
insertion_sort(data)
"""
77 22 88 44 55 66 10
0   1  2  3  4 5  6

pass1: 22 77 44 55 66 10 88    sc=5
pass2: 22 44 55 66 10 77 88    sc=4
pass3: 22 44 55 10 66 77 88    sc=1
pass4: 22 44 10 55 66 77 88    sc=1
pass5: 22 10 44 55 66 77 88    sc=1
pass5: 10 22 44 55 66 77 88    sc=1
pass6: 10 22 44 55 66 77 88    sc=1











"""
