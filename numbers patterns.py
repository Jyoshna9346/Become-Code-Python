'''
num=int(input())
for i in range(1,num+1):
    for j in range(1,num+1):
        print(i,end=" ")
    print()

5
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5 
'''
'''
num=int(input())
for i in range(1,num+1):
    for j in range(1,num+1):
        print(i+j,end=" ")
    print()
5
2 3 4 5 6 
3 4 5 6 7 
4 5 6 7 8 
5 6 7 8 9 
6 7 8 9 10 
>>> 
========
6
2 3 4 5 6 7 
3 4 5 6 7 8 
4 5 6 7 8 9 
5 6 7 8 9 10 
6 7 8 9 10 11 
7 8 9 10 11 12
'''
'''
num=int(input())
for i in range(1,num+1):
    if i%2:
        for j in range(1,num+1):
            print(j,end=" ")
        else:
            for j in range(num,0,-1):
                print(j,end=" ")
        print()

7
1 2 3 4 5 6 7 7 6 5 4 3 2 1 
1 2 3 4 5 6 7 7 6 5 4 3 2 1 
1 2 3 4 5 6 7 7 6 5 4 3 2 1 
1 2 3 4 5 6 7 7 6 5 4 3 2 1 
>>> 
=========
8
1 2 3 4 5 6 7 8 8 7 6 5 4 3 2 1 
1 2 3 4 5 6 7 8 8 7 6 5 4 3 2 1 
1 2 3 4 5 6 7 8 8 7 6 5 4 3 2 1 
1 2 3 4 5 6 7 8 8 7 6 5 4 3 2 1 
>>>
'''
'''
num=int(input())
for i in range(1,num+1):
    if i%2:
        x=1
        y=num
        d=1
    else:
        x=num
        y=1
        d=-1
    for j in range(x,y+d,d):
        print(j,end=" ")
    print()

6
1 2 3 4 5 6 
6 5 4 3 2 1 
1 2 3 4 5 6 
6 5 4 3 2 1 
1 2 3 4 5 6 
6 5 4 3 2 1 
'''
'''
num=int(input())
for i in range(1,num+1):
    if i%2:
        for j in range(1,num+1):
            print(i,end=" ")
    else:
        for j in range(1,num+1):
            print(j,end=" ")
    print()
7
1 1 1 1 1 1 1 
1 2 3 4 5 6 7 
3 3 3 3 3 3 3 
1 2 3 4 5 6 7 
5 5 5 5 5 5 5 
1 2 3 4 5 6 7 
7 7 7 7 7 7 7
'''
    
num=int(input())
for i in range(1,num+1):
    temp=1
    for j in range(1,num+1):
        print(temp,end=" ")
        if temp==0:
            temp=1
        else:
            temp=0
    print()

 8
1 0 1 0 1 0 1 0 
1 0 1 0 1 0 1 0 
1 0 1 0 1 0 1 0 
1 0 1 0 1 0 1 0 
1 0 1 0 1 0 1 0 
1 0 1 0 1 0 1 0 
1 0 1 0 1 0 1 0 
1 0 1 0 1 0 1 0
'''
