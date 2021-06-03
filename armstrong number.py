num=int(input())
def armstrong(num):
    count=0
    temp1=num
    temp2=num
    while num:
        num=num//10
        count+=1
    res=0
##print("no of digits=",count)
    while temp1:
        r=temp1%10
        temp1=temp1//10
        res=res+pow(r,count)
    if res==temp2:
        print("armstrong number")
    else:
       print("not armstrong number")
armstrong(num)

    
