
'''
n=int(input())
data=[None for i in range(n)]
for i in range(n):
    val=int(input())
    data[i]=val
print(data)

'''
'''
n=int(input())
data=list(map(int,input().split()))
print(data)
'''


#INDEX BASED LIST
'''
n=int(input())
data=list(map(int,input().split()))
for i in range(n):
    print(data[i],end='')
'''

#VALUE BASED LIST PROGRAM
'''
n=int(input())
data=list(map(int,input().split()))
for i in range(n):
    print(i,end="")
'''

#TOTAL SUM OF LIST USING FUNCTIONS
'''
def total_marks(n,data):
    res=0
    for i in data:
        res+=i
    return res
n=int(input())
data=list(map(int,input().split()))
total=total_marks(n,data)
print(total)

6
1 2 3 4 5 6 
21
'''
#COUNTING EVEN AND ODD NUMBER IN A LIST

def total_marks(n,data):
    ec=0
    oc=0
    for i in range(n):
        if data[i]%2:
            ec+=1
        else:
            oc+=1
        return ec,oc
n=int(input())
data=list(map(int,input().split()))
total=total_marks(n,data)
for i in total:
    print(i,end="")




        


    
          


