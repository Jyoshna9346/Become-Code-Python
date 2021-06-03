


#findprimes and nonprimes in give data
'''import math as m
def isprime(num):
    if num==0:
        return 0
    s=int(m.sqrt(num))
    for i in range(2,s+1):
        if num%i==0:
            return 0
    return 1
def findprime(n,data):
    prime=[]
    nonprime=[]
    for i in data:
        if isprime(i):
            prime.append(i)
        else:
            nonprime.append(i)
    return prime,nonprime

n=int(input())
data=list(map(int,input().split()))
p,np=findprime(n,data)
print(*np)
print(*p)


5
11 33 46 17 9
33 46 9
11 17 '''
