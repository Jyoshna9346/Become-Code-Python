'''
n=int(input())
while True:
    print(n,end=" ")
    if n==1:
        break
    if n%2:
        n=3*n+1
    else:
        n=n//2
    
7
7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1

'''
'''
def seq(n):
    if n==1:
        print(n,end=" ")
        return
    print(n,end=" ")
    if n%2:
        seq(3*n+1)
    else:
        seq(n//2)
n=int(input())
seq(n)

12
12 6 3 10 5 16 8 4 2 1 
>>> 
========
6
6 3 10 5 16 8 4 2 1 
>>>
'''
'''
def seq(n):
    if n%2:
        return 3*n+1
    return n//2
n=int(input())
print(n,end=" ")
while(n:=seq(n)):
    print(n,end=" ")
    if n==1:
        break
'''

