def original(n,data):
    d=[]
    for i in data:
        if i not in d:
            d.append(i)
    return d
n=int(input())
data=list(map(int,input().split()))
b=original(n,data)
print(*b)


10
4 3 1 5 2 6 3 2 6 7
4 3 1 5 2 6 7
