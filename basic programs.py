'''
num,r1,r2=map(int,input().split())
if r1<=r2:
    while r1<=r2:
        print(num,"x",r1,"=",num*r1)
        r1+=1
else:
    while r2<=r1:
        print(num,"x",r2,"=",num*r2)
        r2+=1

5 1  10
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50

'''


#SAME AS ABOVE PROGRAM IN REVERSE ORDER ALSO
'''
num,r1,r2=map(int,input().split())
inc=1
if r1>r2:
    inc=-1
for i in range(r1,r2+inc,inc):
    print(num,"x",i,"=",num*i)

5 1 10
          
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
'''

#PRINTING A TABLE AND HOW MANY TIMES AND WHERE TO STOP AND WHICH IS DIVISIBLE BY BOTH 3 AND 5
'''
num1,num2,r1=map(int,input().split())
for i in range(1,r1+1):
    if i%num2 and i&num1:
        print(num1,num1*i)
'''

#DIGIT COUNT OF A NUMBER
'''
num=int(input())
dc=0
if num==0:
    dc+=1
else:
    while num:
        r=num%10
        num=num//10
        dc+=1
print(dc)

12345
5
'''

#EVEN AND ODD COUNT OF A NUMBER
'''
n=int(input())
ec=0
oc=0
while n:
    r=n%10
    n=n//10
    if r%2:
        oc+=1
    else:
        ec+=1
print(ec,oc)

12345
2 3
'''
'''
num=int(input())
ec=0
oc=0
while num:
    r=num%10
    num=num//10
    if r%2:
        oc+=1
    else:
        ec+=1
if oc%2==1 and ec%2==0:
    print("even odd")
elif ec%2==0:
    print("even")
elif oc%2:
    print("odd")
else:
    print("mixed")
'''

#PROGRAM FOR PRINTING EVEN AND ODD SEPARTELY FOR A NUMBER
'''
num=int(input())
even=0
odd=0
ec=1
oc=1
while num:
    r=num%10
    num=num//10
    if r%2:
        odd=odd+r*oc
        oc=oc*10
    else:
        even=even+r*ec
        ec=ec*10
print(even,odd)

123
2 13
'''
#IN A NUMBER REPLACE A VALUE  WITH ANOTHER VALUE
'''
num,sv,rv=map(int,input().split())
newnum=0
c=1
while num:
    r=num%10
    num=num//10
    if r==sv:
       r=rv
    newnum=newnum+r*c
    c=c*10
print(newnum)

'''
#IN A NUMBER MUYIPLES OF SEARCH VALUE IS REPLACED BY REPLACE VALUE BY SPECIFING THE REPLACE VALUES

'''
num,sv,rv=map(int,input().split())
rev=0
while num:
    r=num%10
    num=num//10
    rev=rev*10+r
num=0
while rev:
    r=rev%10
    rev=rev//10if r%sv==0:
        r=rv
        rv+=1
        if rv==10:
            rv=1
    num=num*10+r
print(num)

'''
#ABOVE CODE "0" IS NOT WORKING BY THIS BELOW CODE FOR "0" ALSO
'''
num,sv,rv=map(int,input().split())
nn=0
temp=num
c=0
if rv>10:
    rv=rv%10+1
while num:
    r=num%10
    num=num//10
    c+=1
num=temp
c=c-1
while True:
    if c==-1 and num==0:
        r=num//pow(10,c)
    num=num%pow(10,c)
    c-=1
    if r%sv==0:
        r=rv
        rv+=1
        if rv==10:
            rv=1
    nn=nn*10+r
print(nn)
'''#PROGRAM FOR A NUMBER IN THAT MIDDLE VALUES REVERSED
'''
n=int(input())
rev=0
1=num%10
c=0
while num:
    r=num%10
    num=num//10
    rev=rev*10+r
    c+=1
rev=rev%pow(10,c-1)
rev=rev//10
rev=rev*10+1
rev=rev%pow(10,c-1)
rev=r*pow(10,c-1)+rev
print(rev)
'''
#FINDING A MAX AND MIN OF A NUMBER
num=int(input())
mi=num%10
ma=num%10
while num:
    r=num%10
    num=num//10
    if r>ma:
        ma=r
    if r<mi:
        mi=r
print(ma,mi)







    
    
