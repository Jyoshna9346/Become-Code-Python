#match code:

def org(n,data):
    a=[]
    for i in data:
        if i not in a:
            a.append(i)
    return a
n=int(input())
data=list(map(int,input().split()))
d=org(n,data)
print(*d)
c=0
for i in range(n):
    if i==len(d):
        break
    if data[i]==d[i]:
        c+=1
print(c)

10
4 3 1 5 2 6 3 6 7
4 3 1 5 2 6 7
6
