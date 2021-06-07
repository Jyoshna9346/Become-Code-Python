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

'''
#printing count of a numbers in a dic
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




