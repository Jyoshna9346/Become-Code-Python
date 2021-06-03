from math import*
def ispronic(n):
    s=int(sqrt(n))
    for i in range(1,s+1):
        if i*(i+1)==n:
            return True
        return False
n=int(input())
print(ispronic(n))
2
True
3
False

#pronic no:which is the product of 2 consective integers that number of the form n(n+1)
