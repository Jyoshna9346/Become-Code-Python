
def pthFactor(n,p):
    k=0
    d=[1,n]
    s=int(math.sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            d.insert(1,n//i)
            d.insert(1,i)
    return d[p-1]
