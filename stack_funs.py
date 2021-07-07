def push(val):
    global st
    global top
    global size
    if top==size-1:
        print("Stack is overflow")
    else:
        top+=1
        st[top]=val
    
def pop():
    global st
    global top
    global size
    if top==-1:
        return "Stack is Underflow"
    val=st[top]
    st[top]=-1
    top-=1
    return val
        
def display():
    global st
    global top
    global size
    if top==-1:
        print("Stack is Underflow")
    for i in range(top,-1,-1):
        print(st[i])

size=int(input())
st=[-1 for _ in range(size)]
top=-1
while(1):
    print("1.Push 2.POP 3.display 4.exit")
    ch=int(input("Enter Ur choice:"))
    if ch==1:
        push(int(input("Enter value to insert:")))
    elif ch==2:
        print(pop())
    elif ch==3:
        display()
    else:
        break



















