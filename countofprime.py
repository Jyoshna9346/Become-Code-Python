'''
def countprimes(n,data):
    pc=0
    for i in range(len(data)):
        for j in range(2,max(data)+1):
            if data[i]>j:
                if data[i]%j==0:
                    break
    else:
        pc+=1
    return pc
'''
'''
n=int(input())
data=list(map(int,input().split()))
pc=countprimes(n,data)
print(pc)

            
def countprimes(n,data):
    lst=[]
    for i in range(len(data)):
        for j in range(2,max(data)+1):
            if data[i]>j:
                if data[i]%j==0:
                    break
    else:
        lst.append(data[i])
print(*lst)
n=int(input())
data=list(map(int,input().split()))
pc=countprimes(n,data)
print(pc)
'''
import math as m
def countprime(n,data):
    def isprime(n):
        if n==1:
            return 0
        s=int(m.sqrt(n))
        for i in range(2,s+1):
            if n%i==0:
                return 0
            return 1
        for i in data:
            pc=0
            if isprime(i):
                pc+=1
        return pc
n=int(input())
data=list(map(int,input().split()))
pc=countprime(n,data)
print(pc)
