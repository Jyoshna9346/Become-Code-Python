##if condition:
##    statement1
##elif condition:
##    statement2
##else:
##    symtax for condition statements

n=int(input())
if n%2!=0:#odd
    print('Weird')
else:#even
    if n>2 and n<=5:
        print('Not Weird')
   elif n>=6 and n<=20:
        print('Weird')
    else:
      print('Not Weird')


#loop
n=int(input())
for i in range(n):
  print(i**2)
square problem#
i=0
for i in range(0,i<=100,1):
    print(i)#we cant make python loop has infinte loop
    
#function
#add
def add(x,y):
   c=x+y
   print(c)
add(10,20)

##sub
def sub(x,y):
    c=x-y
  print(c)

#mul
def mul(x,y):
   c=x*y
   print(c)
#div
def div(x,y):
    c=x/y
  print(c)

def main():
    add(10,20)
   sub(30,20)
   div(10,5)

if   __name__=='__main___':
    main()
'''
#leap year (want to write program)
#recurrsion
#list comprissions
x=int(input())#1
y=int(input())#1
z=int(input())#1
n=int(input())#2
data1=[]#i,j,k
data=[]
for i in range(x+1):#i=0
    for j in range(y+1):#j=0
        data=[]
       for k in range(z+1):#z=0
           data.append(i)
           data.append(j)
            data.append(k)
           data1.append(data)
            data=[]
n=int(input())
arr=map(int,input.split())
arr=list(set(arr))
arr.sort()
print(arr)

'''

import string
n=int(input())#3-->c
alpha=string.ascii_lowercase
l=[]
for i in range(n):
    s="-".join(alpha[i:n])   
    l.append((s[::-1]+s[1:]).center(4*n-3,'-'))
print(l)
for i in range(len(l)-1,0,-1):
    print(l[i])
for j in range(len(l)):
    print(l[j])



'''
s="BANANA"
k=0
s1=0
a='AELDU'
for i in range(len(s)):
    if s[i] in a:
        k+=len(s)-i
    else:
      s1+len(s)-i
   if k>s1:
      print('Kevin',k)
    elif s1>k:
        print('Stuart',s1)
    else:
       print('Draw')
           
'''       

#find a string
ml=len(string)
s1=len(sub_string)
c=0


for i in range(ml-s1+1):
    if(string[i:(sl)]==sub_string):
        c=c+1
    return c
