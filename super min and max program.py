#supermin program
'''
def reverse(num):
    rev=0
    while num:
        r=num%10
        num=num//10
        rev=rev*10+r
    return rev
def findmin(n,data):
    s=min(data)
    r=reverse(s)
    print(r)
    for i in range(n):
        if data[i]==s:
            data[i]=r
    s=min(data)
    return s==r
n=int(input())
data=list(map(int,input().split()))
minval=findmin(n,data)
print(minval)
'''
6
11 44 55 66 77 88
11
True

'''
min and max
6
12 23 43 56 12 51
12--->21--super min
56-->65---super max
'''
def reverse(num):
    rev=0
    while num:
        r=num%10
        num=num//10
        rev=rev*10+r
    return rev
def findmin(n,data):
    s=max(data)
    r=reverse(s)
    print(r)
    for i in range(n):
        if data[i]==s:
            data[i]=r
    s=max(data)
    return s==r
n=int(input())
data=list(map(int,input().split()))
maxval=findmin(n,data)
print(maxval)
5
22 34 56 78 99
99
True
