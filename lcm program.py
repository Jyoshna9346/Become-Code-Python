'''
def lcm(a,b):
    m=max(a,b)
    for i in range(m,a*b+1):
        if i%a==0 and i%b==0:
            return i
a,b=map(int,input().split())
print(lcm(a,b))

2 3
6
'''
'''
def lcm(a,b):
    m=max(a,b)
    while True:
        print(m)
        if m%a==0 and m%b==0:
            return m
        else:
            m+=1
a,b=map(int,input().split())
print(lcm(a,b))
2 3
3
4
5
6
6
>>> 
=======
6 8
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
24
'''
'''
def lcm(a,b,t):
    if a<t or b<t:
        return a*b
    if a%t==0 and b%t==0:
        return t*lcm(a//t,b//t,t)
    else:
        return lcm(a,b,t+1)
a,b=map(int,input().split())
print(lcm(a,b,2))

2 3
6
>>>
'''
