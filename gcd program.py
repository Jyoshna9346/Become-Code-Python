
def gcd(a,b):
    while b:
        if a>b:
            a,b=b,a
        b=b%a
    return a
a,b=map(int,input().split())
print(gcd(a,b))

7 8
1
>>> 
========
88 24
8

