#useing dictionary
'''
dic={123: "jyoshna",124: "manasa",125: "chandu",113: "chandra"}

for k in dic.keys():
    print(k,dic[k])

for v in dic.values():
    print(v)

for k,v in dic.items():
    print(k,v)


123 jyoshna 
124 manasa
125 chandu
113 chandra
jyoshna
manasa
chandu
chandra
123 jyoshna
124 manasa
125 chandu
113 chandra

'''

#printing count of a numbers in a dic
'''
n=int(input())
data=list(map(int,input().split()))
dic={}
for i in data:
    if i not in dic.keys():
        dic[i]=1
    else:
        dic[i]+=1
for k in dic.keys():
    print(k,dic[k])

17
    
1 2 3 4 3 2 1 4 5 4 3 2 4 5 1 2 3 
1 3
2 4
3 4
4 4
5 2
'''
#printing max values in a dic
'''
n=int(input())
data=list(map(int,input().split()))
dic={}
m=0
for i in data:
    if i not in dic.keys():
        dic[i]=1
    else:
        dic[i]+=1
    if m<dic[i]:
        m=dic[i]
for k in dic.keys():
    if dic[k]==m:
        print(k,dic[k])

        
17
1 2 3 4 3 2 1 4 5 4 3 2 4 5 1 2 3 
2 4
3 4
4 4
'''
'''
s=input()
n=len(s)
print(s)

for i in range(n):
    print(s[i],end="")
print()
for i in s:
    print(i,end="")


this is python class
this is python class
this is python class
this is python class
'''
#it prints alphabets values
'''
s=input()
a=[0]*26
for i in s:
    print(ord(i))

q
113
a
97
A
65
'''
'''
s=input()
a=[0]*26
A=[0]*26
for i in s:
    if i!=' ':
        a[ord(i)-97]+=1
print(a)

jyoshna likes instagram
[3, 0, 0, 0, 1, 0, 1, 1, 2, 1, 1, 1, 1, 2, 1, 0, 0, 1, 3, 1, 0, 0, 0, 0, 1, 0]

this is python class
[1, 0, 1, 0, 0, 0, 0, 2, 2, 0, 0, 1, 0, 1, 1, 1, 0, 0, 4, 2, 0, 0, 0, 0, 1, 0]

'''
#prints letters count in given sentences 
'''
s=input()
dic={}
for i in s:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)

this is python class
{'t': 2, 'h': 2, 'i': 2, 's': 4, ' ': 3, 'p': 1, 'y': 1, 'o': 1, 'n': 1, 'c': 1, 'l': 1, 'a': 1}

'''
#it prints letters in ascending order
'''
s=input()
a=[0]*26
for i in s:
    if i!=' ':
        a[ord(i)-97]+=1
for i in range(26):
    if a[i]!=0:
        print(chr(i+97))
this is python class
a
c
h
i
l
n
o
p
s
t
y

'''
'''
s=input()
data=s.split()
print(len(data))

this is python class
4
'''
'''
s=input()
data=s.split()
for i in data:
    print(len(i))
this is python class
4
2
6
5
'''
'''
s=input()
data=s.split()
l=0
pos=0
for i in range(len(data)):
    if len(data[i])>1:
        l=len(data[i])
        pos=i
print(pos+1,data[pos],1)

this is python class
4 class 1
'''
#printing a sentences in reverse order
'''
s=input()
s=s[::-1]
print(s)

this is python class
ssalc nohtyp si siht
'''
#printing each word in sentence in reverse order
'''
def fun(s):
    data=s.split()
    s=' '
    for w in data:
        s=s+' '+w[::-1]
    return s
s=input()
s=fun(s)
print(s)


this is python class
siht si nohtyp ssalc

'''
#OR
'''
def fun(s):
    data=s.split()
    s=' '
    for i in range(len(data)):
        data[i]=data[i][::-1]
    return ' '.join(data)
s=input()
s=fun(s)
print(s)
'''
def fun(s):
    data=s.split()
    i=0
    j=len(data)-1
    while(i <j):
        data[i],data[j]=data[j],data[i]
        i+=1
        j-+1
    return ' '.join(data)
s=input()
s=fun(s)
print(s)

