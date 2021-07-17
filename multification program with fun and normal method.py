#multiplication program
'''
a,b=map(int,input().split())
res=0
while a:
    if a%2:
        res+=b
    a=a//2
    b=b*2
print(res)

13 24
312
>>> 
12 12
144
>>> 
44 55
2420

'''
#above program using function
'''
def mul(a,b,res=0):
    while a:
        if a%2:
            res+=b
        a=a//2
        b=b*2
    return res
a,b=map(int,input().split())
res=mul(a,b)
print(res)

12 12
144
