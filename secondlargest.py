#secondlargest

def secondlargest(n,data):
    sh,fh=data[0],data[0]
    for i in data[1:]:
            if i>fh:
                sh=fh
                fh=i
            if i>sh and i<fh:
                sh=i
    return sh
n=int(input())
data=list(map(int,input().split()))
print(secondlargest(n,data))

'''
4
1 2 7 8
7
'''
