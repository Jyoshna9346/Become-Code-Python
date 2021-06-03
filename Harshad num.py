def is_Harshad(n):
    s=0
    temp=n
    while n:
        r=n%10
        n=n//10
        s=s+r
    if temp%s==0:
        return True
    return False
n=int(input())
print(is_Harshad(n))

#no which is divisible by the sum of its digits when wrriten in that base
66
False
>>> 
==========
20
True
>>> 
