'''
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()

o/p
5
*****
*****
*****
*****
*****
'''


'''
n=int(input()) 
for i in range(1,n+1): 
    for j in range(1,i+1):
        print("*",end=" ")
    print()         
o/p:
5
*
**
***
****
*****
'''
'''

*
**
***
****
*****
'''
'''
n=int(input())
for i in range(1,n+1):
    for j in range'''
'''
n=int(input())
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
    print()

o/p:
5
    *
   **
  ***
 ****
*****
'''
'''
n=int(input())
for i in range(n,0,-1):
    for j in range(n,i,-1):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
    print()

o/p:
*****
 ****
  ***
   **
    *
'''
'''for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print()

o/p:
*****
****
***
**
*
'''
'''
n=int(input())
for i in range(1,n+1):
    for j in range(n+1,i+1,-1):
        print(" ",end="")
    for k in range(i):
        print(i,end="")
    print()
o/p:
5
     1
    22
   333
  4444
 55555
'''
'''
n=int(input())
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range(n-i):
        print(n-i,end="")
    print()
o/p:
55555
 4444
  333
   22
    1
'''
'''
n=int(input())
for i in range(1,n+1):
    for j in range(n+1,i+1,-1):
        print("",end="")
    for k in range(i):
        print(i,end="")
    print()
o\p:
1    
22
333
4444
55555
'''
'''
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print()

o\p:
1
12
123
1234
12345
123456
'''
'''
n=int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end='')
    print()
o\p:
1234567
123456
123451234
123
12
1
'''
'''
n=int(input())
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end='')
    print()
o/p:
54321
4321
321
21
1
'''
'''
n=int(input())
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()

o/p:
54321
4321
321
21
1
'''
'''
n=int(input())
for i in range(1,1+n):
    for j in range(1,i+1):
        if 1==j:
            print(i,end="")
        else:
            print(j,end="")
    print()
o/p:
5

1
22
323
4234
52345
'''






#special pattern
''''
n=int(input())
for i in range(1,n+1):
    for a in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()

0/p:
5
    *
   ***
  *****
 *******
*********
'''
''''
n=int(input())
for i in range(1,n+1):
    for a in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        print(j,end="")
    print()

o/p:

    1
   123
  12345
 1234567
123456789

'''
'''
n=int(input())
for i in range(1,n+1):
    for a in range(1,n-i+1):
            print(" ",end="")
    for j in range(1,2*i):
            print(i,end="")
    print()

o/p:
    1
   222
  33333
 4444444
555555555
'''



