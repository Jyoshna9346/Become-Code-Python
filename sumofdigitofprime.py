#sumofdigitofnumber
def sumofdigits(data):
    s=0
    j=0
    for i in data:
        while i:
            r=i%10
            i=i//10
            s=s+r
        data[j]=s
        s=0
        j+=1
n=int(input())
data=list(map(int,input().split()))
sumofdigits(data)
print(*data)

 =============================================
5
11 17 13 8 13 
2 8 4 8 4
