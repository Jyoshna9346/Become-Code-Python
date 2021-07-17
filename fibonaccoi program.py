def fibi(a,b,d,num):
    if d>num:
        return
    if d==1 and d<=num:
        print(a,end=" ")
        d+=1
    if d==2 and d<num:
        print(b,end=" ")
    if d<=num:
        print(a+b,end=" ")
    fibi(b,a+b,d+1,num)
num=int(input())
fibi(0,1,1,num)

8
0 1 1 2 3 5 8 13 21

it is commonly denoted as Fn ...from a sequence called the fibonaccci sequence such
that each number is the sum of the two preceding once,staring from 0 and 
