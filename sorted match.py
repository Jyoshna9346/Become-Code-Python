def sort_org_list(n,data):
    d=list(set(data))
    d.sort()
    return d
n=int(input())
data=list(map(int,input().split()))
res=sort_org_list(n,data)
print(*res)
c=0
for i in range(n):
    if i==len(res):
        break
    if data[i]==res[i]:
        c+=1
print(c)


10
4 3 1 5 2 6 3 6 7
1 2 3 4 5 6 7
1
