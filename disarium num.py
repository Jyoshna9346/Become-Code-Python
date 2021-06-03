
'''
def is_disarium(n):
    c=0
    temp=n
    s=0
    while n:
        n=n//10
        c+=1
    n=temp
    while n:
        r=n%10
        n=n//10
        s=s+pow(r,c)
        c-=1
    return s==temp
n=int(input())
print(is_disarium(n))
 ===================================================
175
True

100
False
'''
def isdisarium(num):
    dc=0
    temp=num
    while(temp):
        temp=temp//10
        dc+=1
        temp=num
        res=0
    while temp:
        r=temp%10
        temp=temp//10
        res=res+pow(r,dc)
        dc-=1
    return res==num
num=int(input())
print(isdisarium(num))
