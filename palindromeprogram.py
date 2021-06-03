#palindromenum
'''
def palindromenums(data):
    s,p,c=0,0,1
    count=0
    for i in data:
        temp=i
        s=0
        while i:
            r=i%10
            i=i//10
            s=s*c+r
            c=10
            if temp==s:
                count+=1
        print(count)
n=int(input())
data=list(map(int,input().split()))
palindromenums(data)
'''

def rev(num):
    rev1=0
    while num:
        r=num%10
        num=num//10
        rev1=rev1*10+r
    return rev1
def reverse(n,data):
    c=0
    for i in range(n):
        data[i]==rev(data[i])
        c+=1
    return c 
n=int(input())
data=list(map(int,input().split()))
c=reverse(n,data)
print(c)


4
121 434 123 222
4

        
