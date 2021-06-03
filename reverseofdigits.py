#reverse the each digit in a program
'''
def reversedigits(data):
    s=0
    c=1
    p=0
    for i in data:
        while i:
            r=i%10
            i=i//10
            s=s*c+r
            c=10
            if i==0:
                data[p]=s
                p+=1
                s=0
    return data
n=int(input())
data=list(map(int,input().split()))
reversedigits(data)
print(*data)
'''
def rev(num):
    rev1=0
    while num:
        r=num%10
        num=num//10
        rev1=rev1*10+r
    return rev1
def reverse(n,data):
    for i in range(n):
        data[i]=rev(data[i])
n=int(input())
data=list(map(int,input().split()))
reverse(n,data)
print(*data)
