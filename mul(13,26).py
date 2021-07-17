def mul(a,b):
    if a==1:
        return b
    if a%2:
        return b+mul(a//2,b*2)
    else:
        return 0+mul(a//2,b*2)
a,b=map(int,input().split())
print(mul(a,b))
'''
12 13
6  26
3  52
1  104
0   0
'''
13 26
338
>>> 
=====
12 13
156
>>> 
